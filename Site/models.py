from django.contrib.auth.models import BaseUserManager
from django.db import models

class GerenciadorUsuarios(BaseUserManager):
    def create_user(self, matricula, cpf, nome_completo, data_nascimento, titulacao, universidade, endereco, bairro,
                    municipio, cep, termos_uso, membro_lipe, password=None, **outros_campos):
        if not cpf or not matricula:
            raise ValueError('Membros da LIPE devem ter um CPF válido.')

        user = self.model(
            cpf=cpf,
            matricula=matricula,
            nome_completo=nome_completo,
            data_nascimento=data_nascimento,
            titulacao=titulacao,
            universidade=universidade,
            endereco=endereco,
            bairro=bairro,
            municipio=municipio,
            cep=cep,
            termos_uso=termos_uso,
            membro_lipe=membro_lipe
            **outros_campos
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matricula, cpf, nome_completo, data_nascimento, titulacao, universidade, endereco, bairro,
                    municipio, cep, termos_uso, membro_lipe, password=None, **outros_campos ):

        outros_campos.setdefault('is_superuser', True)
        outros_campos.setdefault('is_staff', True)
        outros_campos.setdefault('is_active', True)

        if outros_campos.get('is_superuser') == False:
            raise ValueError('Um Superusuário deve ter "is_superuser" definido como "True".')

        if outros_campos.get('is_staff') == False:
            raise ValueError('Um Superusuário deve ter "is_staff" definido como "True".')

        user = self.model(
            cpf=cpf,
            matricula=matricula,
            nome_completo=nome_completo,
            data_nascimento=data_nascimento,
            titulacao=titulacao,
            universidade=universidade,
            endereco=endereco,
            bairro=bairro,
            municipio=municipio,
            cep=cep,
            termos_uso=termos_uso,
            membro_lipe=membro_lipe
                        ** outros_campos
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

#class Titulacao():

#class Usuario(AbstractBaseUser, PermissionsMixin):