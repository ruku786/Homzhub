from .registry_class import InheritableClassType
from .models import *
import csv
import io
from django.db import IntegrityError
from .exceptions import CSVException
from django import forms

class BaseCSVClass(metaclass=InheritableClassType):
    class Meta:
        name = None
        description = None
        columns = None

    @classmethod
    def info(cls):
        return {"job_name": cls.Meta.name}

    @classmethod
    def validate_headers(cls, headers):
        columns = cls.Meta.columns
        columns_str = ", ".join(columns)
        if set(columns) != set(headers):
            raise CSVException(f"Invalid Headers in CSV, Allowed headers are {columns_str}")

    @classmethod
    def read_csv(cls, csv_file):
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        data_list = [{k: v for k, v in x.items()}
                     for x in
                     csv.DictReader(io_string, skipinitialspace=True)]
        return data_list

    @classmethod
    def execute(cls, csv_file):
        data_set = cls.read_csv(csv_file)
        if data_set:
            cls.validate_headers(data_set[0].keys())
            upload = cls.upload_csv(data_set)
            return upload
        return None

    @classmethod
    def upload_csv(cls, rows):
        raise NotImplementedError("Upload CSV method not implemented")


class UsersUserService(BaseCSVClass):
    class Meta:
        name = "UsersUser"
        columns = (
              'password',
              'last_login',
              'is_superuser',
              'is_staff',
              'is_active',
              'date_joined',
              'id',
              'first_name',
              'last_name',
              'full_name',
              'email',
              'phone_code',
              'phone_number',
              'social_image_url',
              'referral_code',
              'blacklisted_reason',
               'other_profession',
               'emergency_contact_name',
               'emergency_contact_phone',
               'emergency_contact_phone_code',
               'emergency_contact_email',
               'email_verified',
               'is_verified',
               'is_blacklisted',
               'last_logout',
               'date_of_birth',
               'verified_date',
               'created_at',
               'deleted_at',
               'profile_picture',
        )

    @classmethod
    def upload_csv(cls, rows):
        try:
            for row in rows:
                _, created = UsersUser.objects.update_or_create(
                    password=row.get("password"),
                    last_login=row.get("last_login"),
                    is_superuser=row.get("is_superuser"),
                    is_staff = row.get("is_staff"),
                    is_active = row.get("is_active"),
                    date_joined = row.get(" date_joined"),
                    id = row.get("id "),
                    first_name = row.get("first_name"),
                    last_name = row.get("last_name"),
                    full_name = row.get("full_name"),
                    email = row.get(" email"),
                    phone_code =row.get("phone_code "),
                    phone_number =row.get("phone_number"),
                    social_image_url=row.get("social_image_url"),
                    referral_code = row.get("referral_code "),
                    blacklisted_reason= row.get("blacklisted_reason"),
                    other_profession = row.get("other_profession"),
                    emergency_contact_name=row.get("emergency_contact_name"),
                    emergency_contact_phone = row.get("emergency_contact_phone"),
                    emergency_contact_phone_code =row.get("emergency_contact_phone_code"),
                    emergency_contact_email =row.get("emergency_contact_email"),
                    email_verified=row.get(" email_verified"),
                    is_verified=row.get("is_verified"),
                    is_blacklisted=row.get("is_blacklisted"),
                    last_logout=row.get("last_logout"),
                    date_of_birth=row.get("date_of_birth"),
                    verified_date=row.get("verified_date"),
                    created_at=row.get("created_at"),
                    deleted_at=row.get("deleted_at"),
                    profile_picture=row.get("profile_picture"),

                )
                print(_)


        except UsersUser.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")

class AccountsGeneralledgerService(BaseCSVClass):
    class Meta:
        name = "AccountsGeneralledger"
        columns = (
            'id',
            'label',
            'notes',
            'payer_name',
            'receiver_name',
            'entry_type',
            'transaction_date',
            'amount',
            'created_at',
            'updated_at',
            'account_type_id',
            'asset_id',
            'attachment_id',
            'created_by_id',
            'reviewer_id',
            'updated_by_id',
            'user_id',
            'currency_id',
            'lease_transaction_id',
            'payment_transaction_id',
            'sale_transaction_id'
        )



    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("user", "created_by", "reviewer", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
           for row in rows:
               usersUser = UsersUser_objs.get(user=row.get('user', 'created_by', 'reviewer', 'updated_by'))
               _, created = AccountsGeneralledger.objects.update_or_create(
                   id= usersUser,
                   label=row.get("label"),
                   notes=row.get("notes"),
                   payer_name=row.get("payer_name"),
                   receiver_name=row.get("receiver_name"),
                   entry_type=row.get("entry_type"),
                   transaction_date=row.get("transaction_date"),
                   amount=row.get("amount"),
                   created_at=row.get("created_at"),
                   updated_at=row.get("updated_at"),
                   account_type_id=row.get("account_type_id"),
                   asset_id=row.get("asset_id"),
                   attachment_id=row.get("attachment_id"),
                   created_by_id=row.get("created_by_id"),
                   reviewer_id=row.get("reviewer_id "),
                   updated_by_id=row.get("updated_by_id"),
                   user_id=row.get("user_id"),
                   currency_id=row.get("currency_id"),
                   lease_transaction_id=row.get("lease_transaction_id"),
                   payment_transaction_id=row.get("payment_transaction_id"),
                   sale_transaction_id=row.get("sale_transaction_id"),



               )
               print(_)


        except AccountsGeneralledger.DoesNotExist:
            pass
        raise forms.ValidationError("Your data saved. but some data already exists.")


class AccountsGeneralledgercategoryService(BaseCSVClass):
    class Meta:
        name = "AccountsGeneralledgercategory"
        columns = (
              'id',
              'entry_type',
              'name',
              'created_at',
              'updated_at',
              'created_by',
              'updated_by'
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by",  "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get( 'created_by', 'updated_by'))
                _, created = AccountsGeneralledgercategory.objects.update_or_create(
                    id= usersuser,
                    entry_type=row.get("entry_type"),
                    name=row.get("name"),
                    created_at=row.get("created_at"),
                    updated_at=row.get("updated_at"),
                    created_by=row.get("created_by"),
                    updated_by=row.get("updated_by"),

                )
                print(_)


        except AccountsGeneralledgercategory.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")




def add_classes_to_server():
    AccountsGeneralledgerService()
    UsersUserService()
    AccountsGeneralledgercategoryService()
