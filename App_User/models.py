from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# 수정 끝
class UserManager(BaseUserManager):    
   
    use_in_migrations = True    
    
    # 수정 끝 
    def create_user(self, email, user_name, password):        
        if not email:            
            raise ValueError('이메일은 필수입니다.')
        if not password:            
            raise ValueError('비밀번호는 필수입니다.')
 
        user = self.model(            
            email=self.normalize_email(email),
            user_name = user_name,
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user

    # 수정 끝
    def create_superuser(self, email, user_name, password):        
    
        user = self.create_user(            
            email = self.normalize_email(email),
            user_name = user_name,                    
            password = password,        
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 

class User(AbstractBaseUser, PermissionsMixin):    

    objects = UserManager()
    
    email = models.EmailField(        
        max_length=255,        
        unique=True,    
    )
    user_name = models.CharField(max_length=30)    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
 
    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['user_name']
 
    def __str__(self):
        return self.email
 
    @property
    def is_staff(self):
        return self.is_admin