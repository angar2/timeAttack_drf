from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    username = models.CharField('사용자 계정', max_length=50, unique =True)
    password = models.CharField('비밀번호', max_length=128)
    email = models.EmailField('이메일 주소', max_length=20)
    fullname = models.CharField('이름', max_length=20)
    join_data = models.DateField('가입일', auto_now_add=True)

    is_active = models.BooleanField(default=True) # 회원 활성화 여부
    is_admin = models.BooleanField(default=False) # 관리자 여부

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label): 
        return True

    @property
    def is_staff(self): 
        return self.is_admin


class UserType(models.Model):
    user = models.OneToOneField(User, verbose_name="유저", on_delete=models.CASCADE)
    type = models.ManyToManyField("Type", verbose_name="타입")

    def __str__(self):
        return f"{self.user.username}"


class Type(models.Model):
    name = models.CharField("타입", max_length=50)

    def __str__(self):
        return self.name