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
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
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


class AccountsPaymenttransactionServices(BaseCSVClass):
    class Meta:
        name = "AccountsPaymenttransaction"
        columns = (
            'id',
            'third_party_name',
            'third_party_email',
            'third_party_phone',
            'is_third_party_registered',
            'other_payment_type',
            'expected_amount',
            'paid_amount',
            'balance_amount',
            'late_fee',
            'remarks',
            'is_scheduled',
            'payment_id',
            'payment_reference_number',
            'payment_signature',
            'other_payment_detail' ,
            'transaction_type',
            'processed_date',
            'payment_schedule_date',
            'payment_due_date',
            'payment_date',
            'created_at',
            'updated_at',
            'payment_attempt_count',
            'asset_id',
            'created_by',
            'currency',
            'lease_transaction',
            'mode_of_payment',
            'ops_user',
            'order_status',
            'payer_user',
            'payment_status',
            'payment_type',
            'receiver_user',
            'ref_payment_txn',
            'sale_transaction',
            'updated_by',
            'user_invoice',
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by", "ops_user", "payer_user", "receiver_user") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by', 'ops_user', 'payer_user"', 'receiver_user'))
                _, created = AccountsPaymenttransaction.objects.update_or_create(
                    id=row.get("id"),
                    user_id=usersuser,
                    third_party_name =row.get("third_party_name"),
                    third_party_email =row.get("third_party_email"),
                    third_party_phone =row.get("third_party_phone"),
                    is_third_party_registered =row.get("is_third_party_registered"),
                    other_payment_type =row.get("other_payment_type"),
                    expected_amount =row.get("expected_amount"),
                    paid_amount =row.get("paid_amount"),
                    balance_amount =row.get("balance_amount"),
                    late_fee =row.get("late_fee"),
                    remarks =row.get("remarks"),
                    is_scheduled =row.get("is_scheduled"),
                    payment_id =row.get("payment_id"),
                    payment_reference_number =row.get("payment_reference_number"),
                    payment_signature =row.get("payment_signature"),
                    other_payment_detail =row.get(" other_payment_detail"),
                    transaction_type =row.get("transaction_type "),
                    processed_date =row.get("processed_date"),
                    payment_schedule_date =row.get("payment_schedule_date"),
                    payment_due_date =row.get("payment_due_date"),
                    payment_date =row.get("payment_date"),
                    created_at =row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    payment_attempt_count =row.get("payment_attempt_count"),
                    asset_id =row.get("asset_id"),
                    created_by =row.get("created_by"),
                    currency =row.get("currency"),
                    lease_transaction =row.get("lease_transaction"),
                    mode_of_payment =row.get(" mode_of_payment"),
                    ops_user =row.get("ops_user"),
                    order_status =row.get("order_status"),
                    payer_user =row.get("payer_user"),
                    payment_status =row.get("payment_status"),
                    payment_type =row.get("payment_type"),
                    receiver_user =row.get("receiver_user"),
                    ref_payment_txn = row.get("ref_payment_txn"),
                    sale_transaction =row.get("sale_transaction"),
                    updated_by =row.get("updated_by"),
                    user_invoice =row.get("user_invoice"),
                )
                print(_)


        except AccountsPaymenttransaction.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


class AccountsUserinvoiceServices(BaseCSVClass):
    class Meta:
        name = "AccountsUserinvoice"
        columns = (
            'id',
            'invoice_no',
            'invoice_title',
            'description',
            'issue_date',
            'due_date',
            'late_fee',
            'total_discount',
            'total_price',
            'tax_amount_1',
            'tax_amount_2',
            'tax_amount_3',
            'created_at',
            'updated_at',
            'created_by',
            'currency',
            'tax_type_1',
            'tax_type_2',
            'tax_type_3',
            'updated_by',
            'user',
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
                _, created = AccountsUserinvoice.objects.update_or_create(
                    id=row.get("id"),
                    user_id=usersuser,
                    invoice_no =row.get("invoice_no"),
                    invoice_title =row.get("invoice_title"),
                    description =row.get("description"),
                    issue_date =row.get("issue_date"),
                    due_date =row.get("due_date"),
                    late_fee = row.get("late_fee"),
                    total_discount =row.get("total_discount"),
                    total_price =row.get("total_price"),
                    tax_amount_1 =row.get("tax_amount_1"),
                    tax_amount_2 =row.get("tax_amount_2"),
                    tax_amount_3 =row.get("tax_amount_3"),
                    created_at =row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    created_by =row.get("created_by"),
                    currency =row.get("currency"),
                    tax_type_1 =row.get("tax_type_1"),
                    tax_type_2 =row.get("tax_type_2"),
                    tax_type_3 =row.get("tax_type_3"),
                    updated_by =row.get("updated_by"),
                    user =row.get("user"),

                )
                print(_)


        except AccountsUserinvoice.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


class AccountsUserinvoiceitemServices(BaseCSVClass):
    class Meta:
        name = "AccountsUserinvoiceitem"
        columns = (
             'item_name',
             'no_of_units',
             'description',
             'unit_price',
             'discount',
             'pos_price',
             'created_at',
             'updated_at',
             'created_by',
             'currency' ,
             'updated_by',
             'user_invoice',
             'user_service_plan',
             'user_value_bundle',
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
                _, created = AccountsUserinvoiceitem.objects.update_or_create(
                    user_id=usersuser,
                    item_name=row.get("item_name"),
                    no_of_units =row.get("no_of_units"),
                    description =row.get("description"),
                    unit_price =row.get("unit_price"),
                    discount =row.get("discount"),
                    pos_price =row.get("pos_price"),
                    created_at = row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    created_by =row.get("created_by"),
                    currency =row.get("currency"),
                    updated_by =row.get("updated_by"),
                    user_invoice =row.get("user_invoice"),
                    user_service_plan =row.get("user_service_plan"),
                    user_value_bundle =row.get("user_value_bundle"),

                )
                print(_)


        except AccountsUserinvoiceitem.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


class AdvertisementsAdvertisementServices(BaseCSVClass):
    class Meta:
        name = "AdvertisementsAdvertisement"
        columns = (
             'id',
             'title',
             'description',
             'link',
             'total_visits',
             'expire_date',
             'created_at',
             'updated_at',
             'attachment',
             'category',
             'created_by',
             'updated_by',
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
                _, created = AdvertisementsAdvertisement.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    title =row.get("title"),
                    description =row.get("description"),
                    link =row.get("link"),
                    total_visits =row.get("total_visits"),
                    expire_date =row.get("expire_date"),
                    created_at =row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    attachment =row.get("attachment"),
                    category =row.get("category"),
                    created_by =row.get("created_by"),
                    updated_by =row.get("updated_by"),


                )
                print(_)


        except AdvertisementsAdvertisement.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


class AssetsAmenityServices(BaseCSVClass):
    class Meta:
        name = "AssetsAmenity"
        columns = (
             'id',
             'name',
             'description',
             'created_at',
             'updated_at',
             'attachment',
             'category',
             'created_by',
             'updated_by',
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
                _, created = AssetsAmenity.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    name =row.get("name"),
                    description =row.get("description"),
                    created_at =row.get("created_at"),
                    updated_at = row.get("updated_at"),
                    attachment =row.get("attachment"),
                    category =row.get("category"),
                    created_by =row.get("created_by"),
                    updated_by =row.get("updated_by"),



                )
                print(_)


        except AssetsAmenity.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


class AssetsAmenitycategoryServices(BaseCSVClass):
    class Meta:
        name = "AssetsAmenitycategory"
        columns = (
             'id',
             'name',
             'created_at',
             'updated_at',
             'created_by',
             'updated_by',
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
                _, created = AssetsAmenitycategory.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    name=row.get("name"),
                    created_at =row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    created_by =row.get("created_by"),
                    updated_by =row.get("updated_by"),


                )
                print(_)


        except AssetsAmenitycategory.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


class AssetsAmenitygroupServices(BaseCSVClass):
    class Meta:
        name = "AssetsAmenitygroup"
        columns = (
             'id',
             'name',
             'created_at',
             'updated_at',
             'created_by',
             'updated_by',
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
                _, created = AssetsAmenitygroup.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    name=row.get("name"),
                    created_at =row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    created_by =row.get("created_by"),
                    updated_by =row.get("updated_by"),


                )
                print(_)


        except AssetsAmenitygroup.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


class AssetsAssetadditionalinfoServices(BaseCSVClass):
    class Meta:
        name = "AssetsAssetadditionalinfo"
        columns = (
             'id',
             'maintenance_amount',
             'maintenance_payment_schedule',
             'society_contact_name',
             'society_office_number',
             'society_email',
             'account_number',
             'ifsc',
             'created_at',
             'updated_at',
             'asset_id',
             'created_by',
             'maintenance_unit',
             'updated_by',
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
                _, created = AssetsAssetadditionalinfo.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    maintenance_amount=row.get("maintenance_amount"),
                    maintenance_payment_schedule =row.get("maintenance_payment_schedule"),
                    society_contact_name =row.get("society_contact_name"),
                    society_office_number =row.get("society_office_number"),
                    society_email =row.get("society_email"),
                    account_number =row.get("account_number"),
                    ifsc =row.get("ifsc"),
                    created_at = row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    asset_id =row.get("asset_id"),
                    created_by = row.get("created_by"),
                    maintenance_unit =row.get("maintenance_unit"),
                    updated_by =row.get("updated_by"),


                )
                print(_)


        except AssetsAssetadditionalinfo.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


class AssetsAssetamenitygroupServices(BaseCSVClass):
    class Meta:
        name = "AssetsAssetamenitygroup"
        columns = (
             'id',
             'created_at',
             'updated_at',
             'amenity',
             'amenity_group',
             'created_by',
             'updated_by',
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
                _, created = AssetsAssetamenitygroup.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    created_at =row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    amenity=row.get("amenity"),
                    amenity_group=row.get("amenity_group"),
                    created_by =row.get("created_by"),
                    updated_by =row.get("updated_by"),


                )
                print(_)


        except AssetsAssetamenitygroup.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")



class AssetsAssetdocumentServices(BaseCSVClass):
    class Meta:
        name = "AssetsAssetdocument"
        columns = (
             'id',
             'description',
             'created_at',
             'updated_at',
             'asset_id',
             'attachment',
             'created_by',
             'lease_listing',
             'sale_listing',
             'updated_by',
             'user',
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by", "user") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by', 'user'))
                _, created = AssetsAssetdocument.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    description =row.get("description"),
                    created_at =row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    asset_id =row.get("asset_id"),
                    attachment =row.get("attachment"),
                    created_by =row.get("created_by"),
                    lease_listing =row.get("lease_listing"),
                    sale_listing =row.get("sale_listing"),
                    updated_by =row.get("updated_by"),
                    user =row.get("user"),



                )
                print(_)


        except AssetsAssetdocument.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


class AssetsAssetgroupServices(BaseCSVClass):
    class Meta:
        name = "AssetsAssetgroup"
        columns = (
             'name',
             'code',
             'created_at',
             'updated_at',
             'created_by',
             'updated_by',
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
                _, created = AssetsAssetgroup.objects.update_or_create(
                    user_id=usersuser,
                    name=row.get("name"),
                    code=row.get("code"),
                    created_at =row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    created_by =row.get("created_by"),
                    updated_by =row.get("updated_by"),


                )
                print(_)


        except AssetsAssetgroup.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")



class AssetsAssetspaceServices(BaseCSVClass):
    class Meta:
        name = "AssetsAssetspace"
        columns = (
             'id',
             'name',
             'description',
             'is_shared',
             'created_at',
             'updated_at',
             'asset_id',
             'created_by',
             'space_type',
             'updated_by',

        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
                _, created = AssetsAssetspace.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    name=row.get("name"),
                    description =row.get("description"),
                    is_shared=row.get("is_shared"),
                    created_at =row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    asset_id =row.get("asset_id"),
                    created_by =row.get("created_by"),
                    space_type=row.get("space_type"),
                    updated_by =row.get("updated_by"),




                )
                print(_)


        except AssetsAssetspace.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


class AssetsAssetspaceattachmentServices(BaseCSVClass):
    class Meta:
        name = "AssetsAssetspaceattachment"
        columns = (
            'description',
            'is_cover_image',
            'created_at',
            'updated_at',
            'asset_id',
            'attachment',
            'created_by',
            'updated_by',

        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
                _, created = AssetsAssetspaceattachment.objects.update_or_create(
                    user_id=usersuser,
                    description=row.get("description"),
                    is_cover_image=row.get("is_cover_image"),
                    created_at=row.get("created_at"),
                    updated_at=row.get("updated_at"),
                    asset_id=row.get("asset_id"),
                    attachment=row.get("attachment"),
                    created_by=row.get("created_by"),
                    updated_by=row.get("updated_by"),

                )
                print(_)


        except AssetsAssetspaceattachment.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


class AssetsAssettypeServices(BaseCSVClass):
    class Meta:
        name = "AssetsAssettype"
        columns = (
            'name',
            'created_at',
            'updated_at',
            'asset_group',
            'created_by',
            'updated_by',

        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
                _, created = AssetsAssettype.objects.update_or_create(
                    user_id=usersuser,
                    name=row.get("name"),
                    created_at=row.get("created_at"),
                    updated_at=row.get("updated_at"),
                    asset_group=row.get("asset_group"),
                    created_by=row.get("created_by"),
                    updated_by=row.get("updated_by"),

                )
                print(_)


        except AssetsAssettype.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


class AssetsAssetuserServices(BaseCSVClass):
    class Meta:
        name = "AssetsAssetuser"
        columns = (
            'id',
            'start_date',
            'end_date',
            'ownership_percentage',
            'is_current',
            'verified_at',
            'created_at',
            'updated_at',
            'asset_id',
            'created_by',
            'updated_by',
            'user',
            'verified_by',

        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by", "user", "verified_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by','user', 'verified_by'))
                _, created = AssetsAssetuser.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    start_date =row.get("start_date"),
                    end_date =row.get("end_date"),
                    ownership_percentage =row.get("ownership_percentage"),
                    is_current =row.get("is_current"),
                    verified_at =row.get("verified_at"),
                    created_at =row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    asset_id =row.get("asset_id"),
                    created_by =row.get("created_by"),
                    updated_by =row.get("updated_by"),
                    user =row.get("user"),
                    verified_by =row.get("verified_by"),


                )
                print(_)


        except AssetsAssetuser.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


class AssetsAssetverificationdocumentServices(BaseCSVClass):
    class Meta:
        name = "AssetsAssetverificationdocument"
        columns = (
            'id',
            'is_expired',
            'created_at',
            'updated_at',
            'verified_at',
            'asset_id',
            'created_by',
            'document',
            'verification_document_type',
            'verified_by',
            'updated_by',

        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by", "verified_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by', 'verified_by'))
                _, created = AssetsAssetverificationdocument.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    is_expired=row.get("is_expired"),
                    created_at=row.get("created_at"),
                    updated_at=row.get("updated_at"),
                    verified_at=row.get("verified_at"),
                    asset_id=row.get("asset_id"),
                    created_by=row.get("created_by"),
                    document=row.get("document"),
                    verification_document_type =row.get("verification_document_type"),
                    verified_by=row.get("verified_by"),
                    updated_by=row.get("updated_by"),

                )
                print(_)


        except AssetsAssetverificationdocument.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")

class AssetsAssetverificationdocumenttypeServices(BaseCSVClass):
    class Meta:
        name = "AssetsAssetverificationdocumenttype"
        columns = (
            'id',
            'is_expired',
            'created_at',
            'updated_at',
            'verified_at',
            'asset_id',
            'created_by',
            'document',
            'verification_document_type',
            'verified_by',
            'updated_by',

        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
                _, created = AssetsAssetverificationdocumenttype.objects.update_or_create(
                    user_id=usersuser,
                    category=row.get("category"),
                    name =row.get("name "),
                    title =row.get("title"),
                    label =row.get("label"),
                    icon =row.get("icon"),
                    help_text =row.get("help_text"),
                    description =row.get("description"),
                    created_at=row.get("created_at"),
                    updated_at=row.get("updated_at"),
                    created_by=row.get("created_by"),
                    updated_by=row.get("updated_by"),

                )
                print(_)


        except AssetsAssetverificationdocumenttype.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")

class AssetsCarpetareaunitServices(BaseCSVClass):
    class Meta:
        name = "AssetsCarpetareaunit"
        columns = (
            'id',
            'name',
            'label',
            'title',
            'base_conversion_factor',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',

        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by'))
                _, created = AssetsCarpetareaunit.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    name =row.get("name "),
                    label=row.get("label"),
                    title =row.get("title"),
                    base_conversion_factor =row.get("base_conversion_factor"),
                    created_at=row.get("created_at"),
                    updated_at=row.get("updated_at"),
                    created_by=row.get("created_by"),
                    updated_by=row.get("updated_by"),

                )
                print(_)


        except AssetsCarpetareaunit.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")

class AssetsLeaselistingServices(BaseCSVClass):
    class Meta:
        name = "AssetsLeaselisting"
        columns = (
            'id',
            'expected_monthly_rent',
            'security_deposit',
            'annual_rent_increment_percentage',
            'minimum_lease_period',
            'maximum_lease_period',
            'rent_free_period',
            'furnishing',
            'maintenance_included',
            'utility_included',
            'available_from_date',
            'end_date',
            'status',
            'description',
            'approved_at',
            'created_at',
            'updated_at',
            'approved_by',
            'created_by',
            'lease_unit',
            'updated_by',
            'currency',

        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by", "approved_by") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by', 'approved_by'))
                _, created = AssetsLeaselisting.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    expected_monthly_rent=row.get("expected_monthly_rent"),
                    security_deposit =row.get("security_deposit"),
                    annual_rent_increment_percentage =row.get("annual_rent_increment_percentage"),
                    minimum_lease_period=row.get("minimum_lease_period"),
                    maximum_lease_period =row.get("maximum_lease_period"),
                    rent_free_period =row.get("rent_free_period"),
                    furnishing =row.get("furnishing"),
                    maintenance_included =row.get("maintenance_included"),
                    utility_included =row.get("utility_included"),
                    available_from_date =row.get("available_from_date"),
                    end_date =row.get("end_date"),
                    status =row.get("status"),
                    description =row.get("description "),
                    approved_at =row.get("approved_at"),
                    created_at =row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    approved_by =row.get("approved_by"),
                    created_by =row.get("created_by"),
                    lease_unit =row.get("lease_unit"),
                    updated_by =row.get("updated_by"),
                    currency =row.get("currency"),


                )
                print(_)


        except AssetsLeaselisting.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")

class AssetsLeaselistingleadServices(BaseCSVClass):
    class Meta:
        name = "AssetsLeaselistinglead"
        columns = (
            'id',
            'spaces',
            'preferred_contact_time',
            'message',
            'contact_person_type',
            'lead_type',
            'is_wishlisted',
            'created_at',
            'updated_at',
            'lead_user',
            'lease_listing',
            'person_contacted',
            'user_search',
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("person_contacted", "lead_user") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('person_contacted', 'lead_user'))
                _, created = AssetsLeaselistinglead.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    spaces=row.get("spaces"),
                    preferred_contact_time =row.get("preferred_contact_time"),
                    message =row.get("message"),
                    contact_person_type =row.get("contact_person_type"),
                    lead_type =row.get("lead_type"),
                    is_wishlisted =row.get("is_wishlisted"),
                    created_at =row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    lead_user =row.get("lead_user"),
                    lease_listing =row.get("lease_listing"),
                    person_contacted =row.get("person_contacted"),
                    user_search =row.get("user_search"),



                )
                print(_)


        except AssetsLeaselistinglead.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


class AssetsLeaselistinguserServices(BaseCSVClass):
    class Meta:
        name = "AssetsLeaselistinguser"
        columns = (
            'id',
            'start_date',
            'end_date',
            'created_at',
            'updated_at',
            'created_by',
            'lease_listing',
            'updated_by',
            'user_representative',
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by", "user_representative") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by', 'user_representative'))
                _, created = AssetsLeaselistinguser.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    start_date=row.get("start_date"),
                    end_date =row.get("end_date"),
                    created_at =row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    created_by =row.get("created_by"),
                    lease_listing = row.get("lease_listing"),
                    updated_by =row.get("updated_by"),
                    user_representative =row.get("user_representative"),




                )
                print(_)


        except AssetsLeaselistinguser.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")

class AssetsLeasenegotiationServices(BaseCSVClass):
    class Meta:
        name = "AssetsLeasenegotiation"
        columns = (
            'id',
            'proposed_rent',
            'proposed_deposit',
            'proposed_lease_period',
            'annual_rent_increment_percentage',
            'maintenance_included',
            'utility_included',
            'status',
            'negotiation_start_date',
            'negotiation_end_date',
            'move_in_date',
            'created_at',
            'updated_at',
            'created_by',
            'lease_listing',
            'potential_tenant',
            'updated_by',
        )

    @classmethod
    def upload_csv(cls, rows):
        UsersUser_user = [x.get("created_by", "updated_by", "potential_tenant") for x in rows]
        UsersUser_objs = UsersUser.objects.filter(user__in=UsersUser_user)
        try:
            for row in rows:
                usersuser = UsersUser_objs.get(user=row.get('created_by', 'updated_by', 'potential_tenant'))
                _, created = AssetsLeasenegotiation.objects.update_or_create(
                    user_id=usersuser,
                    id=row.get("id"),
                    proposed_rent=row.get("proposed_rent"),
                    proposed_deposit =row.get("proposed_deposit"),
                    proposed_lease_period =row.get("proposed_lease_period"),
                    annual_rent_increment_percentage =row.get("annual_rent_increment_percentage"),
                    maintenance_included =row.get("maintenance_included"),
                    utility_included =row.get("utility_included"),
                    status =row.get("status"),
                    negotiation_start_date =row.get("negotiation_start_date"),
                    negotiation_end_date =row.get("negotiation_end_date"),
                    move_in_date =row.get("move_in_date"),
                    created_at =row.get("created_at"),
                    updated_at =row.get("updated_at"),
                    created_by =row.get("created_by"),
                    lease_listing =row.get("lease_listing"),
                    potential_tenant =row.get("potential_tenant"),
                    updated_by =row.get("updated_by"),





                )
                print(_)


        except AssetsLeasenegotiation.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")


def add_classes_to_server():
    AccountsGeneralledgerService()
    UsersUserService()
    AccountsGeneralledgercategoryService()
    AccountsPaymenttransactionServices()
    AccountsUserinvoiceServices()
    AccountsUserinvoiceitemServices()
    AdvertisementsAdvertisementServices()
    AssetsAmenityServices()
    AssetsAmenitycategoryServices()
    AssetsAmenitygroupServices()
    AssetsAssetadditionalinfoServices()
    AssetsAssetamenitygroupServices()
    AssetsAssetdocumentServices()
    AssetsAssetgroupServices()
    AssetsAssetspaceServices()
    AssetsAssetspaceattachmentServices()
    AssetsAssettypeServices()
    AssetsAssetuserServices()
    AssetsAssetverificationdocumentServices()
    AssetsAssetverificationdocumenttypeServices()
    AssetsCarpetareaunitServices()
    AssetsLeaselistingServices()
    AssetsLeaselistingleadServices()
    AssetsLeaselistinguserServices()
    AssetsLeasenegotiationServices()
