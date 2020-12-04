# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsGeneralledger(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    payer_name = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    entry_type = models.CharField(max_length=100)
    transaction_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=15, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    account_type = models.ForeignKey('AccountsGeneralledgercategory', models.DO_NOTHING)
    asset_id = models.BigIntegerField()
    attachment = models.ForeignKey('AttachmentsAttachment', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="account_created_by")
    currency = models.ForeignKey('GenericsCountrycurrency', models.DO_NOTHING)
    lease_transaction = models.ForeignKey('AssetsLeasetransaction', models.DO_NOTHING, blank=True, null=True)
    payment_transaction = models.ForeignKey('AccountsPaymenttransaction', models.DO_NOTHING, blank=True, null=True)
    reviewer = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    sale_transaction = models.ForeignKey('AssetsSaletransaction', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="user_accounts")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="accounts_user")
    base_amount = models.DecimalField(max_digits=15, decimal_places=3)
    exchange_rate = models.DecimalField(max_digits=9, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'accounts_generalledger'


class AccountsGeneralledgerHistory(models.Model):
    id = models.BigIntegerField()
    label = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    payer_name = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    entry_type = models.CharField(max_length=100)
    transaction_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=15, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    account_type_id = models.BigIntegerField(blank=True, null=True)
    asset_id = models.BigIntegerField(blank=True, null=True)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    payment_transaction_id = models.BigIntegerField(blank=True, null=True)
    reviewer_id = models.BigIntegerField(blank=True, null=True)
    sale_transaction_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    base_amount = models.DecimalField(max_digits=15, decimal_places=3)
    exchange_rate = models.DecimalField(max_digits=9, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'accounts_generalledger_history'


class AccountsGeneralledgercategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    entry_type = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="created_by_user")
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_generalledgercategory'


class AccountsGeneralledgercategoryHistory(models.Model):
    id = models.BigIntegerField()
    entry_type = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_generalledgercategory_history'


class AccountsPaymenttransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    third_party_name = models.CharField(max_length=255)
    third_party_email = models.CharField(max_length=255)
    third_party_phone = models.CharField(max_length=255)
    is_third_party_registered = models.BooleanField()
    other_payment_type = models.CharField(max_length=255)
    expected_amount = models.DecimalField(max_digits=15, decimal_places=3)
    paid_amount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    balance_amount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    late_fee = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    remarks = models.CharField(max_length=255)
    is_scheduled = models.BooleanField()
    payment_id = models.CharField(max_length=255)
    payment_reference_number = models.CharField(max_length=255)
    payment_signature = models.CharField(max_length=255)
    other_payment_detail = models.TextField()  # This field type is a guess.
    transaction_type = models.CharField(max_length=10)
    processed_date = models.DateTimeField(blank=True, null=True)
    payment_schedule_date = models.DateTimeField()
    payment_due_date = models.DateTimeField()
    payment_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    payment_attempt_count = models.SmallIntegerField()
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    currency = models.ForeignKey('GenericsCountrycurrency', models.DO_NOTHING)
    lease_transaction = models.ForeignKey('AssetsLeasetransaction', models.DO_NOTHING, blank=True, null=True)
    mode_of_payment = models.ForeignKey('ListOfValuesListofvalue', models.DO_NOTHING, blank=True, null=True)
    ops_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="user_ops_user")
    order_status = models.ForeignKey('ListOfValuesListofvalue', models.DO_NOTHING, blank=True, null=True, related_name="order_status")
    payer_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="user_payer")
    payment_status = models.ForeignKey('ListOfValuesListofvalue', models.DO_NOTHING, blank=True, null=True, related_name="payment_status")
    payment_type = models.ForeignKey('ListOfValuesListofvalue', models.DO_NOTHING, blank=True, null=True, related_name="payment_type")
    receiver_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="user_receiver")
    ref_payment_txn = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    sale_transaction = models.ForeignKey('AssetsSaletransaction', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_payment")
    user_invoice = models.ForeignKey('AccountsUserinvoice', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_paymenttransaction'


class AccountsPaymenttransactionHistory(models.Model):
    id = models.BigIntegerField()
    third_party_name = models.CharField(max_length=255)
    third_party_email = models.CharField(max_length=255)
    third_party_phone = models.CharField(max_length=255)
    is_third_party_registered = models.BooleanField()
    other_payment_type = models.CharField(max_length=255)
    expected_amount = models.DecimalField(max_digits=15, decimal_places=3)
    paid_amount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    balance_amount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    late_fee = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    remarks = models.CharField(max_length=255)
    is_scheduled = models.BooleanField()
    payment_id = models.CharField(max_length=255)
    payment_reference_number = models.CharField(max_length=255)
    payment_signature = models.CharField(max_length=255)
    other_payment_detail = models.TextField()  # This field type is a guess.
    transaction_type = models.CharField(max_length=10)
    processed_date = models.DateTimeField(blank=True, null=True)
    payment_schedule_date = models.DateTimeField()
    payment_due_date = models.DateTimeField()
    payment_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    payment_attempt_count = models.SmallIntegerField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    mode_of_payment_id = models.BigIntegerField(blank=True, null=True)
    ops_user_id = models.BigIntegerField(blank=True, null=True)
    order_status_id = models.BigIntegerField(blank=True, null=True)
    payer_user_id = models.BigIntegerField(blank=True, null=True)
    payment_status_id = models.BigIntegerField(blank=True, null=True)
    payment_type_id = models.BigIntegerField(blank=True, null=True)
    receiver_user_id = models.BigIntegerField(blank=True, null=True)
    ref_payment_txn_id = models.BigIntegerField(blank=True, null=True)
    sale_transaction_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_invoice_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_paymenttransaction_history'


class AccountsUserinvoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice_no = models.CharField(unique=True, max_length=18)
    invoice_title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    issue_date = models.DateTimeField()
    due_date = models.DateTimeField()
    late_fee = models.DecimalField(max_digits=15, decimal_places=3)
    total_discount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    total_price = models.DecimalField(max_digits=15, decimal_places=3)
    tax_amount_1 = models.DecimalField(max_digits=15, decimal_places=3)
    tax_amount_2 = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    tax_amount_3 = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    currency = models.ForeignKey('GenericsCountrycurrency', models.DO_NOTHING)
    tax_type_1 = models.ForeignKey('GenericsTaxtype', models.DO_NOTHING)
    tax_type_2 = models.ForeignKey('GenericsTaxtype', models.DO_NOTHING, blank=True, null=True, related_name="tax_type2")
    tax_type_3 = models.ForeignKey('GenericsTaxtype', models.DO_NOTHING, blank=True, null=True, related_name="tax_type_3")
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_invoice")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="user_invoice")

    class Meta:
        managed = False
        db_table = 'accounts_userinvoice'


class AccountsUserinvoiceHistory(models.Model):
    id = models.BigIntegerField()
    invoice_no = models.CharField(max_length=18)
    invoice_title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    issue_date = models.DateTimeField()
    due_date = models.DateTimeField()
    late_fee = models.DecimalField(max_digits=15, decimal_places=3)
    total_discount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    total_price = models.DecimalField(max_digits=15, decimal_places=3)
    tax_amount_1 = models.DecimalField(max_digits=15, decimal_places=3)
    tax_amount_2 = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    tax_amount_3 = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    tax_type_1_id = models.BigIntegerField(blank=True, null=True)
    tax_type_2_id = models.BigIntegerField(blank=True, null=True)
    tax_type_3_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_userinvoice_history'


class AccountsUserinvoiceitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    no_of_units = models.SmallIntegerField()
    description = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=15, decimal_places=3)
    discount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    pos_price = models.DecimalField(max_digits=15, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    currency = models.ForeignKey('GenericsCountrycurrency', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="invoice_updated_by_user")
    user_invoice = models.ForeignKey(AccountsUserinvoice, models.DO_NOTHING)
    user_service_plan = models.ForeignKey('ServicesUserserviceplan', models.DO_NOTHING, blank=True, null=True)
    user_value_bundle = models.ForeignKey('ServicesUservaluebundle', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_userinvoiceitem'


class AccountsUserinvoiceitemHistory(models.Model):
    id = models.BigIntegerField()
    item_name = models.CharField(max_length=100)
    no_of_units = models.SmallIntegerField()
    description = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=15, decimal_places=3)
    discount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    pos_price = models.DecimalField(max_digits=15, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_invoice_id = models.BigIntegerField(blank=True, null=True)
    user_service_plan_id = models.BigIntegerField(blank=True, null=True)
    user_value_bundle_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_userinvoiceitem_history'


class AdvertisementsAdvertisement(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=200)
    total_visits = models.IntegerField()
    expire_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment = models.ForeignKey('AttachmentsAttachment', models.DO_NOTHING)
    category = models.ForeignKey('ListOfValuesListofvalue', models.DO_NOTHING)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True,related_name="updated_by_user_advertisement")

    class Meta:
        managed = False
        db_table = 'advertisements_advertisement'


class AdvertisementsAdvertisementHistory(models.Model):
    id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=200)
    total_visits = models.IntegerField()
    expire_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    category_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advertisements_advertisement_history'


class AssetsAmenity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment = models.ForeignKey('AttachmentsAttachment', models.DO_NOTHING)
    category = models.ForeignKey('AssetsAmenitycategory', models.DO_NOTHING)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_assetammenity")

    class Meta:
        managed = False
        db_table = 'assets_amenity'


class AssetsAmenitycategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_category")

    class Meta:
        managed = False
        db_table = 'assets_amenitycategory'


class AssetsAmenitygroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_group")

    class Meta:
        managed = False
        db_table = 'assets_amenitygroup'


class AssetsAssetadditionalinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    maintenance_amount = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    maintenance_payment_schedule = models.CharField(max_length=20, blank=True, null=True)
    society_contact_name = models.CharField(max_length=255)
    society_office_number = models.CharField(max_length=20)
    society_email = models.CharField(max_length=254, blank=True, null=True)
    account_number = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    maintenance_unit = models.ForeignKey('ListOfValuesListofvalue', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_additional")

    class Meta:
        managed = False
        db_table = 'assets_assetadditionalinfo'


class AssetsAssetadditionalinfoHistory(models.Model):
    id = models.BigIntegerField()
    maintenance_amount = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    maintenance_payment_schedule = models.CharField(max_length=20, blank=True, null=True)
    society_contact_name = models.CharField(max_length=255)
    society_office_number = models.CharField(max_length=20)
    society_email = models.CharField(max_length=254, blank=True, null=True)
    account_number = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    maintenance_unit_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_assetadditionalinfo_history'


class AssetsAssetamenitygroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    amenity = models.ForeignKey(AssetsAmenity, models.DO_NOTHING)
    amenity_group = models.ForeignKey(AssetsAmenitygroup, models.DO_NOTHING)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_amenity")

    class Meta:
        managed = False
        db_table = 'assets_assetamenitygroup'


class AssetsAssetdocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    attachment = models.ForeignKey('AttachmentsAttachment', models.DO_NOTHING)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    lease_listing = models.ForeignKey('AssetsLeaselisting', models.DO_NOTHING, blank=True, null=True)
    sale_listing = models.ForeignKey('AssetsSalelisting', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_doc")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="user_doc")

    class Meta:
        managed = False
        db_table = 'assets_assetdocument'


class AssetsAssetdocumentHistory(models.Model):
    id = models.BigIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_assetdocument_history'


class AssetsAssetgroup(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(unique=True, max_length=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_asset_group")

    class Meta:
        managed = False
        db_table = 'assets_assetgroup'


class AssetsAssetgroupHistory(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_assetgroup_history'


class AssetsAssetgroupspacetype(models.Model):
    view_on_add = models.BooleanField()
    asset_group = models.ForeignKey(AssetsAssetgroup, models.DO_NOTHING)
    space_type = models.ForeignKey('AssetsSpacetype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assets_assetgroupspacetype'


class AssetsAssetgroupspacetypeHistory(models.Model):
    id = models.IntegerField()
    view_on_add = models.BooleanField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_group_id = models.IntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    space_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_assetgroupspacetype_history'


class AssetsAssetspace(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=40)
    is_shared = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    space_type = models.ForeignKey('AssetsSpacetype', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_asset_space")

    class Meta:
        managed = False
        db_table = 'assets_assetspace'


class AssetsAssetspaceattachment(models.Model):
    description = models.TextField()
    is_cover_image = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    attachment = models.ForeignKey('AttachmentsAttachment', models.DO_NOTHING)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_spaceattachment")

    class Meta:
        managed = False
        db_table = 'assets_assetspaceattachment'


class AssetsAssetspaceattachmentHistory(models.Model):
    id = models.IntegerField()
    description = models.TextField()
    is_cover_image = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_assetspaceattachment_history'


class AssetsAssettype(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_group = models.ForeignKey(AssetsAssetgroup, models.DO_NOTHING)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_assettype")

    class Meta:
        managed = False
        db_table = 'assets_assettype'


class AssetsAssettypeHistory(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_group_id = models.IntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_assettype_history'


class AssetsAssetuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    ownership_percentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    is_current = models.BooleanField()
    verified_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_asset_user")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="user_asset")
    verified_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="asset_verified_by")

    class Meta:
        managed = False
        db_table = 'assets_assetuser'


class AssetsAssetuserHistory(models.Model):
    id = models.BigIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    ownership_percentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    is_current = models.BooleanField()
    verified_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    verified_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_assetuser_history'


class AssetsAssetverificationdocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_expired = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    verified_at = models.DateTimeField(blank=True, null=True)
    asset_id = models.BigIntegerField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    document = models.ForeignKey('AttachmentsAttachment', models.DO_NOTHING)
    verification_document_type = models.ForeignKey('AssetsAssetverificationdocumenttype', models.DO_NOTHING)
    verified_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="verified_by_user")
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_document")

    class Meta:
        managed = False
        db_table = 'assets_assetverificationdocument'


class AssetsAssetverificationdocumentHistory(models.Model):
    id = models.BigIntegerField()
    is_expired = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    verified_at = models.DateTimeField(blank=True, null=True)
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    document_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    verification_document_type_id = models.IntegerField(blank=True, null=True)
    verified_by_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_assetverificationdocument_history'


class AssetsAssetverificationdocumenttype(models.Model):
    category = models.CharField(max_length=10)
    name = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    icon = models.CharField(max_length=50)
    help_text = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_verification")

    class Meta:
        managed = False
        db_table = 'assets_assetverificationdocumenttype'


class AssetsAssetverificationdocumenttypeHistory(models.Model):
    id = models.IntegerField()
    category = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    icon = models.CharField(max_length=50)
    help_text = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_assetverificationdocumenttype_history'


class AssetsCarpetareaunit(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    label = models.CharField(unique=True, max_length=50)
    title = models.CharField(unique=True, max_length=50, blank=True, null=True)
    base_conversion_factor = models.DecimalField(max_digits=18, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_carpet")

    class Meta:
        managed = False
        db_table = 'assets_carpetareaunit'


class AssetsCarpetareaunitHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    title = models.CharField(max_length=50, blank=True, null=True)
    base_conversion_factor = models.DecimalField(max_digits=18, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_carpetareaunit_history'


class AssetsLeaselisting(models.Model):
    id = models.BigAutoField(primary_key=True)
    expected_monthly_rent = models.DecimalField(max_digits=15, decimal_places=3)
    security_deposit = models.DecimalField(max_digits=15, decimal_places=3)
    annual_rent_increment_percentage = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    minimum_lease_period = models.SmallIntegerField()
    maximum_lease_period = models.SmallIntegerField(blank=True, null=True)
    rent_free_period = models.SmallIntegerField(blank=True, null=True)
    furnishing = models.CharField(max_length=10)
    maintenance_included = models.BooleanField()
    utility_included = models.BooleanField()
    available_from_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)
    description = models.TextField()
    approved_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    approved_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="listing_approved_by")
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    lease_unit = models.ForeignKey('AssetsLeaseunit', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_assets_lease")
    currency = models.ForeignKey('GenericsCountrycurrency', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assets_leaselisting'


class AssetsLeaselistingHistory(models.Model):
    id = models.BigIntegerField()
    expected_monthly_rent = models.DecimalField(max_digits=15, decimal_places=3)
    security_deposit = models.DecimalField(max_digits=15, decimal_places=3)
    annual_rent_increment_percentage = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    minimum_lease_period = models.SmallIntegerField()
    maximum_lease_period = models.SmallIntegerField(blank=True, null=True)
    rent_free_period = models.SmallIntegerField(blank=True, null=True)
    furnishing = models.CharField(max_length=10)
    maintenance_included = models.BooleanField()
    utility_included = models.BooleanField()
    available_from_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)
    description = models.TextField()
    approved_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    approved_by_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lease_unit_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_leaselisting_history'


class AssetsLeaselistinglead(models.Model):
    id = models.BigAutoField(primary_key=True)
    spaces = models.TextField()  # This field type is a guess.
    preferred_contact_time = models.TextField()  # This field type is a guess.
    message = models.CharField(max_length=255)
    contact_person_type = models.CharField(max_length=50, blank=True, null=True)
    lead_type = models.CharField(max_length=10)
    is_wishlisted = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    lead_user = models.ForeignKey('UsersUser', models.DO_NOTHING)
    lease_listing = models.ForeignKey(AssetsLeaselisting, models.DO_NOTHING)
    person_contacted = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="lease_person_contacted")
    user_search = models.ForeignKey('AssetsUsersearch', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_leaselistinglead'


class AssetsLeaselistingleadHistory(models.Model):
    id = models.BigIntegerField()
    spaces = models.TextField()  # This field type is a guess.
    preferred_contact_time = models.TextField()  # This field type is a guess.
    message = models.CharField(max_length=255)
    contact_person_type = models.CharField(max_length=50, blank=True, null=True)
    lead_type = models.CharField(max_length=10)
    is_wishlisted = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lead_user_id = models.BigIntegerField(blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    person_contacted_id = models.BigIntegerField(blank=True, null=True)
    user_search_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_leaselistinglead_history'


class AssetsLeaselistingtenantpreference(models.Model):
    lease_listing = models.ForeignKey(AssetsLeaselisting, models.DO_NOTHING)
    tenant_preference = models.ForeignKey('AssetsTenantpreference', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assets_leaselistingtenantpreference'


class AssetsLeaselistinguser(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    lease_listing = models.ForeignKey(AssetsLeaselisting, models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_leaselisting")
    user_representative = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="user_representative")

    class Meta:
        managed = False
        db_table = 'assets_leaselistinguser'


class AssetsLeaselistinguserHistory(models.Model):
    id = models.BigIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_representative_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_leaselistinguser_history'


class AssetsLeasenegotiation(models.Model):
    id = models.BigAutoField(primary_key=True)
    proposed_rent = models.DecimalField(max_digits=18, decimal_places=4)
    proposed_deposit = models.DecimalField(max_digits=18, decimal_places=4)
    proposed_lease_period = models.SmallIntegerField()
    annual_rent_increment_percentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    maintenance_included = models.BooleanField()
    utility_included = models.BooleanField()
    status = models.CharField(max_length=20)
    negotiation_start_date = models.DateTimeField()
    negotiation_end_date = models.DateTimeField(blank=True, null=True)
    move_in_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    lease_listing = models.ForeignKey(AssetsLeaselisting, models.DO_NOTHING)
    potential_tenant = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="potential_tenant")
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_lease_negotiation")

    class Meta:
        managed = False
        db_table = 'assets_leasenegotiation'


class AssetsLeasenegotiationHistory(models.Model):
    id = models.BigIntegerField()
    proposed_rent = models.DecimalField(max_digits=18, decimal_places=4)
    proposed_deposit = models.DecimalField(max_digits=18, decimal_places=4)
    proposed_lease_period = models.SmallIntegerField()
    annual_rent_increment_percentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    maintenance_included = models.BooleanField()
    utility_included = models.BooleanField()
    status = models.CharField(max_length=20)
    negotiation_start_date = models.DateTimeField()
    negotiation_end_date = models.DateTimeField(blank=True, null=True)
    move_in_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    potential_tenant_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_leasenegotiation_history'


class AssetsLeasetenant(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    feedback = models.CharField(max_length=255)
    rental_stay_rating = models.CharField(max_length=255)
    is_blacklisted = models.BooleanField()
    blacklisted_reasons = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    lease_transaction = models.ForeignKey('AssetsLeasetransaction', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_lease_tenant")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="user_lease")

    class Meta:
        managed = False
        db_table = 'assets_leasetenant'


class AssetsLeasetenantHistory(models.Model):
    id = models.BigIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    feedback = models.CharField(max_length=255)
    rental_stay_rating = models.CharField(max_length=255)
    is_blacklisted = models.BooleanField()
    blacklisted_reasons = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_leasetenant_history'


class AssetsLeasetransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    rent = models.DecimalField(max_digits=18, decimal_places=4)
    security_deposit = models.DecimalField(max_digits=18, decimal_places=4)
    lease_period = models.SmallIntegerField()
    annual_rent_increment_percentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    maintenance_included = models.BooleanField()
    utility_included = models.BooleanField()
    status = models.CharField(max_length=20)
    lease_start_date = models.DateTimeField()
    lease_end_date = models.DateTimeField()
    agreement_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    lease_listing = models.ForeignKey(AssetsLeaselisting, models.DO_NOTHING, blank=True, null=True)
    lease_unit = models.ForeignKey('AssetsLeaseunit', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_transaction")
    currency = models.ForeignKey('GenericsCountrycurrency', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assets_leasetransaction'


class AssetsLeasetransactionHistory(models.Model):
    id = models.BigIntegerField()
    rent = models.DecimalField(max_digits=18, decimal_places=4)
    security_deposit = models.DecimalField(max_digits=18, decimal_places=4)
    lease_period = models.SmallIntegerField()
    annual_rent_increment_percentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    maintenance_included = models.BooleanField()
    utility_included = models.BooleanField()
    status = models.CharField(max_length=20)
    lease_start_date = models.DateTimeField()
    lease_end_date = models.DateTimeField()
    agreement_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    lease_unit_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_leasetransaction_history'


class AssetsLeaseunit(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    description = models.TextField()
    asset_id = models.BigIntegerField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_leaseunit")

    class Meta:
        managed = False
        db_table = 'assets_leaseunit'


class AssetsLeaseunitHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    description = models.TextField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_leaseunit_history'


class AssetsLeaseunitdetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_space = models.ForeignKey(AssetsAssetspace, models.DO_NOTHING)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    lease_unit = models.ForeignKey(AssetsLeaseunit, models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_lease")

    class Meta:
        managed = False
        db_table = 'assets_leaseunitdetail'


class AssetsLeaseunitdetailHistory(models.Model):
    id = models.BigIntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_space_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lease_unit_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_leaseunitdetail_history'


class AssetsListingvisit(models.Model):
    id = models.BigAutoField(primary_key=True)
    visit_type = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    comments = models.TextField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    lead = models.ForeignKey('LeadsLead', models.DO_NOTHING)
    lease_listing = models.ForeignKey(AssetsLeaselisting, models.DO_NOTHING, blank=True, null=True)
    sale_listing = models.ForeignKey('AssetsSalelisting', models.DO_NOTHING, blank=True, null=True)
    scheduled_by = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="scheduled_by")
    scheduled_for = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="scheduled_for")
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_visit")

    class Meta:
        managed = False
        db_table = 'assets_listingvisit'


class AssetsListingvisitHistory(models.Model):
    id = models.BigIntegerField()
    visit_type = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    comments = models.TextField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lead_id = models.BigIntegerField(blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    scheduled_by_id = models.BigIntegerField(blank=True, null=True)
    scheduled_for_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_listingvisit_history'


class AssetsProject(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_amenity_group = models.ForeignKey(AssetsAssetamenitygroup, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_project")

    class Meta:
        managed = False
        db_table = 'assets_project'


class AssetsProjectHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_amenity_group_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_project_history'


class AssetsRenttransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    rent_month = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=50)
    rent_amount = models.DecimalField(max_digits=15, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    lease_transaction = models.ForeignKey(AssetsLeasetransaction, models.DO_NOTHING)
    lease_unit = models.ForeignKey(AssetsLeaseunit, models.DO_NOTHING)
    payment_transaction = models.ForeignKey(AccountsPaymenttransaction, models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_rent")

    class Meta:
        managed = False
        db_table = 'assets_renttransaction'


class AssetsRenttransactionHistory(models.Model):
    id = models.BigIntegerField()
    rent_month = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=50)
    rent_amount = models.DecimalField(max_digits=15, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    lease_unit_id = models.BigIntegerField(blank=True, null=True)
    payment_transaction_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_renttransaction_history'


class AssetsSalelisting(models.Model):
    id = models.BigAutoField(primary_key=True)
    expected_price = models.DecimalField(max_digits=15, decimal_places=3)
    expected_booking_amount = models.DecimalField(max_digits=15, decimal_places=3)
    available_from_date = models.DateField()
    booking_amount_grace_period = models.SmallIntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)
    description = models.TextField()
    approved_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    approved_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="approved_by_sale")
    asset_id = models.BigIntegerField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_asset")
    currency = models.ForeignKey('GenericsCountrycurrency', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assets_salelisting'


class AssetsSalelistingHistory(models.Model):
    id = models.BigIntegerField()
    expected_price = models.DecimalField(max_digits=15, decimal_places=3)
    expected_booking_amount = models.DecimalField(max_digits=15, decimal_places=3)
    available_from_date = models.DateField()
    booking_amount_grace_period = models.SmallIntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)
    description = models.TextField()
    approved_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    approved_by_id = models.BigIntegerField(blank=True, null=True)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_salelisting_history'


class AssetsSalelistinglead(models.Model):
    id = models.BigAutoField(primary_key=True)
    spaces = models.TextField()  # This field type is a guess.
    preferred_contact_time = models.TextField()  # This field type is a guess.
    message = models.CharField(max_length=255)
    contact_person_type = models.CharField(max_length=50, blank=True, null=True)
    lead_type = models.CharField(max_length=10)
    is_wishlisted = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    lead_user = models.ForeignKey('UsersUser', models.DO_NOTHING)
    person_contacted = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="person_contacted_sale")
    sale_listing = models.ForeignKey(AssetsSalelisting, models.DO_NOTHING)
    user_search = models.ForeignKey('AssetsUsersearch', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_salelistinglead'


class AssetsSalelistingleadHistory(models.Model):
    id = models.BigIntegerField()
    spaces = models.TextField()  # This field type is a guess.
    preferred_contact_time = models.TextField()  # This field type is a guess.
    message = models.CharField(max_length=255)
    contact_person_type = models.CharField(max_length=50, blank=True, null=True)
    lead_type = models.CharField(max_length=10)
    is_wishlisted = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lead_user_id = models.BigIntegerField(blank=True, null=True)
    person_contacted_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    user_search_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_salelistinglead_history'


class AssetsSalelistinguser(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    sale_listing = models.ForeignKey(AssetsSalelisting, models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_salelisting")
    user_representative = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="user_sale")

    class Meta:
        managed = False
        db_table = 'assets_salelistinguser'


class AssetsSalelistinguserHistory(models.Model):
    id = models.BigIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_representative_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_salelistinguser_history'


class AssetsSalenegotiation(models.Model):
    id = models.BigAutoField(primary_key=True)
    proposed_price = models.DecimalField(max_digits=18, decimal_places=4)
    proposed_booking_amount = models.DecimalField(max_digits=18, decimal_places=4)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    potential_buyer = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="potential_buyer")
    sale_listing = models.ForeignKey(AssetsSalelisting, models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_sale")

    class Meta:
        managed = False
        db_table = 'assets_salenegotiation'


class AssetsSalenegotiationHistory(models.Model):
    id = models.BigIntegerField()
    proposed_price = models.DecimalField(max_digits=18, decimal_places=4)
    proposed_booking_amount = models.DecimalField(max_digits=18, decimal_places=4)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    potential_buyer_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_salenegotiation_history'


class AssetsSaletransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=18, decimal_places=4)
    booking_amount = models.DecimalField(max_digits=18, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    buyer = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="buyer")
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    sale_listing = models.ForeignKey(AssetsSalelisting, models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user")
    currency = models.ForeignKey('GenericsCountrycurrency', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assets_saletransaction'


class AssetsSaletransactionHistory(models.Model):
    id = models.BigIntegerField()
    price = models.DecimalField(max_digits=18, decimal_places=4)
    booking_amount = models.DecimalField(max_digits=18, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    buyer_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_saletransaction_history'


class AssetsSpacetype(models.Model):
    name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20)
    is_primary = models.BooleanField()
    is_mandatory = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment = models.ForeignKey('AttachmentsAttachment', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_space")

    class Meta:
        managed = False
        db_table = 'assets_spacetype'


class AssetsSpacetypeHistory(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20)
    is_primary = models.BooleanField()
    is_mandatory = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_spacetype_history'


class AssetsTenantpreference(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_type = models.ForeignKey(AssetsAssettype, models.DO_NOTHING)
    country = models.ForeignKey('GenericsCountry', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    region = models.ForeignKey('GenericsRegion', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_tenants")

    class Meta:
        managed = False
        db_table = 'assets_tenantpreference'


class AssetsTenantpreferenceHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_type_id = models.IntegerField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_tenantpreference_history'


class AssetsUsersearch(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_guest = models.BooleanField()
    search_latitude = models.DecimalField(max_digits=10, decimal_places=8)
    search_longitude = models.DecimalField(max_digits=10, decimal_places=8)
    asset_transaction_type = models.TextField()
    device_type = models.CharField(max_length=255)
    browser_type = models.CharField(max_length=255)
    asset_type = models.TextField()  # This field type is a guess.
    user_location_latitude = models.DecimalField(max_digits=10, decimal_places=8)
    user_location_longitude = models.DecimalField(max_digits=10, decimal_places=8)
    ip_address = models.GenericIPAddressField()
    results_count = models.IntegerField()
    min_price = models.BigIntegerField()
    max_price = models.BigIntegerField()
    furnishing_status = models.CharField(max_length=10)
    room_count = models.TextField()  # This field type is a guess.
    bath_count = models.TextField()  # This field type is a guess.
    is_verified = models.BooleanField()
    miscellaneous_search_criteria = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_group = models.ForeignKey(AssetsAssetgroup, models.DO_NOTHING)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_usersearch'


class AssetsUsersearchHistory(models.Model):
    id = models.BigIntegerField()
    is_guest = models.BooleanField()
    search_latitude = models.DecimalField(max_digits=10, decimal_places=8)
    search_longitude = models.DecimalField(max_digits=10, decimal_places=8)
    asset_transaction_type = models.TextField()
    device_type = models.CharField(max_length=255)
    browser_type = models.CharField(max_length=255)
    asset_type = models.TextField()  # This field type is a guess.
    user_location_latitude = models.DecimalField(max_digits=10, decimal_places=8)
    user_location_longitude = models.DecimalField(max_digits=10, decimal_places=8)
    ip_address = models.GenericIPAddressField()
    results_count = models.IntegerField()
    min_price = models.BigIntegerField()
    max_price = models.BigIntegerField()
    furnishing_status = models.CharField(max_length=10)
    room_count = models.TextField()  # This field type is a guess.
    bath_count = models.TextField()  # This field type is a guess.
    is_verified = models.BooleanField()
    miscellaneous_search_criteria = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_group_id = models.IntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_usersearch_history'


class AttachmentsAttachment(models.Model):
    id = models.BigAutoField(primary_key=True)
    original_name = models.CharField(max_length=255)
    unique_name = models.CharField(unique=True, max_length=255)
    attachment_type = models.CharField(max_length=100)
    mime_type = models.CharField(max_length=150)
    link = models.CharField(max_length=255)
    size_in_bytes = models.IntegerField()
    media_attributes = models.TextField()  # This field type is a guess.
    is_associated = models.BooleanField()
    is_public = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_attachments")

    class Meta:
        managed = False
        db_table = 'attachments_attachment'


class AttachmentsAttachmentHistory(models.Model):
    id = models.BigIntegerField()
    original_name = models.CharField(max_length=255)
    unique_name = models.CharField(max_length=255)
    attachment_type = models.CharField(max_length=100)
    mime_type = models.CharField(max_length=150)
    link = models.CharField(max_length=255)
    size_in_bytes = models.IntegerField()
    media_attributes = models.TextField()  # This field type is a guess.
    is_associated = models.BooleanField()
    is_public = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachments_attachment_history'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)



class ClientSupportClientsupport(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    raised_by = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="raised_by_client")
    support_category = models.ForeignKey('ListOfValuesListofvalue', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_client")

    class Meta:
        managed = False
        db_table = 'client_support_clientsupport'


class ClientSupportClientsupportHistory(models.Model):
    id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    raised_by_id = models.BigIntegerField(blank=True, null=True)
    support_category_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_support_clientsupport_history'


class ClientSupportClientsupportattachment(models.Model):
    id = models.BigAutoField(primary_key=True)
    attachment = models.OneToOneField(AttachmentsAttachment, models.DO_NOTHING)
    client_support = models.ForeignKey(ClientSupportClientsupport, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'client_support_clientsupportattachment'


class ClientSupportClientsupportattachmentHistory(models.Model):
    id = models.BigIntegerField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    client_support_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_support_clientsupportattachment_history'


class CustomersCustomer(models.Model):
    schema_name = models.CharField(unique=True, max_length=63)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customers_customer'


class CustomersDomain(models.Model):
    domain = models.CharField(unique=True, max_length=253)
    is_primary = models.BooleanField()
    tenant = models.ForeignKey(CustomersCustomer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'customers_domain'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoExceptionCodesCustomerrorcode(models.Model):
    id = models.BigAutoField(primary_key=True)
    error_key = models.CharField(unique=True, max_length=255)
    error_code = models.SmallIntegerField(unique=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_exception_codes_customerrorcode'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoQOrmq(models.Model):
    key = models.CharField(max_length=100)
    payload = models.TextField()
    lock = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_q_ormq'


class DjangoQSchedule(models.Model):
    func = models.CharField(max_length=256)
    hook = models.CharField(max_length=256, blank=True, null=True)
    args = models.TextField(blank=True, null=True)
    kwargs = models.TextField(blank=True, null=True)
    schedule_type = models.CharField(max_length=1)
    repeats = models.IntegerField()
    next_run = models.DateTimeField(blank=True, null=True)
    task = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    minutes = models.SmallIntegerField(blank=True, null=True)
    cron = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_q_schedule'


class DjangoQTask(models.Model):
    name = models.CharField(max_length=100)
    func = models.CharField(max_length=256)
    hook = models.CharField(max_length=256, blank=True, null=True)
    args = models.TextField(blank=True, null=True)
    kwargs = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    started = models.DateTimeField()
    stopped = models.DateTimeField()
    success = models.BooleanField()
    id = models.CharField(primary_key=True, max_length=32)
    group = models.CharField(max_length=100, blank=True, null=True)
    attempt_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_q_task'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GenericsCity(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    region = models.ForeignKey('GenericsRegion', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'generics_city'


class GenericsCompany(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    long_name = models.CharField(max_length=255)
    email_domain = models.CharField(unique=True, max_length=255)
    hq_address_line_1 = models.CharField(max_length=255)
    hq_address_line_2 = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=15)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    location = models.ForeignKey('GenericsLocation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'generics_company'


class GenericsCountry(models.Model):
    name = models.CharField(max_length=255)
    iso2_code = models.CharField(unique=True, max_length=2)
    iso3_code = models.CharField(unique=True, max_length=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'generics_country'


class GenericsCountrycurrency(models.Model):
    currency_code = models.CharField(max_length=3)
    currency_name = models.CharField(max_length=255)
    currency_symbol = models.CharField(max_length=50)
    sub_unit_currency = models.CharField(max_length=100)
    sub_unit_conversion_factor = models.DecimalField(max_digits=10, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    country = models.ForeignKey(GenericsCountry, models.DO_NOTHING)
    is_primary = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'generics_countrycurrency'


class GenericsCountryphonecode(models.Model):
    phone_code = models.CharField(max_length=10)
    is_primary = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    country = models.ForeignKey(GenericsCountry, models.DO_NOTHING)
    phone_number_max_length = models.SmallIntegerField()
    phone_number_min_length = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'generics_countryphonecode'


class GenericsExchangerate(models.Model):
    id = models.BigAutoField(primary_key=True)
    source_currency = models.CharField(max_length=3)
    target_currency = models.CharField(max_length=3)
    exchange_rate = models.DecimalField(max_digits=9, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'generics_exchangerate'
        unique_together = (('source_currency', 'target_currency'),)


class GenericsLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    city_name = models.CharField(max_length=255)
    region_name = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    iso2_code = models.CharField(max_length=2)
    iso3_code = models.CharField(max_length=3)
    phone_codes = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    city = models.ForeignKey(GenericsCity, models.DO_NOTHING)
    country = models.ForeignKey(GenericsCountry, models.DO_NOTHING)
    region = models.ForeignKey('GenericsRegion', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'generics_location'
        unique_together = (('city', 'region', 'country'), ('city_name', 'region_name', 'country_name'),)


class GenericsRegion(models.Model):
    name = models.CharField(max_length=255)
    region_code = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    country = models.ForeignKey(GenericsCountry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'generics_region'


class GenericsTaxtype(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    description = models.TextField()
    tax_percentage = models.DecimalField(max_digits=6, decimal_places=3)
    effective_start_date = models.DateTimeField()
    effective_end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    country = models.ForeignKey(GenericsCountry, models.DO_NOTHING)
    region = models.ForeignKey(GenericsRegion, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'generics_taxtype'
        unique_together = (('name', 'region'),)


class LeadsLead(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_code = models.CharField(max_length=10)
    primary_phone_number = models.CharField(max_length=20)
    secondary_phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255)
    is_corporate = models.BooleanField()
    min_budget = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    max_budget = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    furnishing_status = models.CharField(max_length=10, blank=True, null=True)
    carpet_area = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    expected_price = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    available_from_date = models.DateTimeField(blank=True, null=True)
    assigned_at = models.DateTimeField(blank=True, null=True)
    comments = models.TextField()
    loe_status = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    amenity_group = models.ForeignKey(AssetsAmenitygroup, models.DO_NOTHING, blank=True, null=True)
    asset_type = models.ForeignKey(AssetsAssettype, models.DO_NOTHING, blank=True, null=True)
    assigned_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="assigned_by")
    assigned_to = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    carpet_area_unit = models.ForeignKey(AssetsCarpetareaunit, models.DO_NOTHING, blank=True, null=True)
    lead_source = models.ForeignKey('ListOfValuesListofvalue', models.DO_NOTHING, related_name="lead_source")
    lead_stage = models.ForeignKey('LeadsLeadstage', models.DO_NOTHING)
    lead_type = models.ForeignKey('ListOfValuesListofvalue', models.DO_NOTHING)
    referred_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="referred_by")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="user_leads")
    user_rep = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="user_rep")

    class Meta:
        managed = False
        db_table = 'leads_lead'


class LeadsLeadHistory(models.Model):
    id = models.BigIntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_code = models.CharField(max_length=10)
    primary_phone_number = models.CharField(max_length=20)
    secondary_phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255)
    is_corporate = models.BooleanField()
    min_budget = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    max_budget = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    furnishing_status = models.CharField(max_length=10, blank=True, null=True)
    carpet_area = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    expected_price = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    available_from_date = models.DateTimeField(blank=True, null=True)
    assigned_at = models.DateTimeField(blank=True, null=True)
    comments = models.TextField()
    loe_status = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    amenity_group_id = models.BigIntegerField(blank=True, null=True)
    asset_type_id = models.IntegerField(blank=True, null=True)
    assigned_by_id = models.BigIntegerField(blank=True, null=True)
    assigned_to_id = models.BigIntegerField(blank=True, null=True)
    carpet_area_unit_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lead_source_id = models.BigIntegerField(blank=True, null=True)
    lead_stage_id = models.BigIntegerField(blank=True, null=True)
    lead_type_id = models.BigIntegerField(blank=True, null=True)
    referred_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    user_rep_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads_lead_history'


class LeadsLeadstage(models.Model):
    id = models.BigAutoField(primary_key=True)
    stage = models.IntegerField()
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_group = models.ForeignKey(AssetsAssetgroup, models.DO_NOTHING)
    lead_txn_type = models.ForeignKey('ListOfValuesListofvalue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'leads_leadstage'


class LeadsLeadstageHistory(models.Model):
    id = models.BigIntegerField()
    stage = models.IntegerField()
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_group_id = models.IntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lead_txn_type_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads_leadstage_history'


class ListOfValuesListofvalue(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_name = models.CharField(max_length=255)
    column_name = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    list_label = models.CharField(max_length=255)
    list_value = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_list")

    class Meta:
        managed = False
        db_table = 'list_of_values_listofvalue'


class ListOfValuesListofvalueHistory(models.Model):
    id = models.BigIntegerField()
    table_name = models.CharField(max_length=255)
    column_name = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    list_label = models.CharField(max_length=255)
    list_value = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    content_type_id = models.IntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'list_of_values_listofvalue_history'


class NotificationsNotification(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    read_at = models.DateTimeField(blank=True, null=True)
    additional_metadata = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField()
    object_id = models.BigIntegerField()
    actor = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    asset_id = models.BigIntegerField(blank=True, null=True)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    lease_listing = models.ForeignKey(AssetsLeaselisting, models.DO_NOTHING, blank=True, null=True)
    notification_type = models.ForeignKey('NotificationsNotificationtype', models.DO_NOTHING)
    sale_listing = models.ForeignKey(AssetsSalelisting, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="user_notifications")

    class Meta:
        managed = False
        db_table = 'notifications_notification'


class NotificationsNotificationHistory(models.Model):
    id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    read_at = models.DateTimeField(blank=True, null=True)
    additional_metadata = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField()
    object_id = models.BigIntegerField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    actor_id = models.BigIntegerField(blank=True, null=True)
    asset_id = models.BigIntegerField(blank=True, null=True)
    content_type_id = models.IntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    notification_type_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications_notification_history'


class NotificationsNotificationtype(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    priority = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment = models.ForeignKey(AttachmentsAttachment, models.DO_NOTHING)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_notification")

    class Meta:
        managed = False
        db_table = 'notifications_notificationtype'


class NotificationsNotificationtypeHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    priority = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications_notificationtype_history'


class ServicesHomzhubpointsdefinition(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit_value = models.IntegerField()
    points_per_unit = models.IntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    category = models.ForeignKey(ListOfValuesListofvalue, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    unit_currency = models.ForeignKey(GenericsCountrycurrency, models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_points")

    class Meta:
        managed = False
        db_table = 'services_homzhubpointsdefinition'


class ServicesHomzhubpointsdefinitionHistory(models.Model):
    id = models.BigIntegerField()
    unit_value = models.IntegerField()
    points_per_unit = models.IntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    category_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    unit_currency_id = models.IntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_homzhubpointsdefinition_history'


class ServicesPromotionrule(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    promo_code = models.CharField(max_length=255)
    promo_communication = models.CharField(max_length=255)
    promotions_per_user = models.SmallIntegerField(blank=True, null=True)
    base_cart_value = models.DecimalField(max_digits=15, decimal_places=3)
    users_limit = models.SmallIntegerField()
    is_active = models.BooleanField(blank=True, null=True)
    discount_value = models.IntegerField()
    promotion_amount_total = models.DecimalField(max_digits=15, decimal_places=3)
    promotion_availed = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_role = models.CharField(max_length=255)
    asset_country = models.ForeignKey(GenericsCountry, models.DO_NOTHING)
    asset_group = models.ForeignKey(AssetsAssetgroup, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="created_by_promotion")
    discount_operator = models.ForeignKey(ListOfValuesListofvalue, models.DO_NOTHING)
    image = models.ForeignKey(AttachmentsAttachment, models.DO_NOTHING, blank=True, null=True)
    promotion_type = models.ForeignKey(ListOfValuesListofvalue, models.DO_NOTHING, related_name="rule_promotion_type")
    sale_city = models.ForeignKey(GenericsCity, models.DO_NOTHING)
    sale_country = models.ForeignKey(GenericsCountry, models.DO_NOTHING, related_name="servicees_sale_country")
    service_plan = models.ForeignKey('ServicesServiceplan', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_promotion")

    class Meta:
        managed = False
        db_table = 'services_promotionrule'


class ServicesPromotionruleHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    promo_code = models.CharField(max_length=255)
    promo_communication = models.CharField(max_length=255)
    promotions_per_user = models.SmallIntegerField(blank=True, null=True)
    base_cart_value = models.DecimalField(max_digits=15, decimal_places=3)
    users_limit = models.SmallIntegerField()
    is_active = models.BooleanField(blank=True, null=True)
    discount_value = models.IntegerField()
    promotion_amount_total = models.DecimalField(max_digits=15, decimal_places=3)
    promotion_availed = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_role = models.CharField(max_length=255)
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_country_id = models.IntegerField(blank=True, null=True)
    asset_group_id = models.IntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    discount_operator_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    image_id = models.BigIntegerField(blank=True, null=True)
    promotion_type_id = models.BigIntegerField(blank=True, null=True)
    sale_city_id = models.IntegerField(blank=True, null=True)
    sale_country_id = models.IntegerField(blank=True, null=True)
    service_plan_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_promotionrule_history'


class ServicesServiceplan(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    tier = models.SmallIntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    min_assets = models.SmallIntegerField()
    max_assets = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_serviceplan")
    upgrade_option = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_serviceplan'


class ServicesServiceplanHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    tier = models.SmallIntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    min_assets = models.SmallIntegerField()
    max_assets = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    upgrade_option_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_serviceplan_history'


class ServicesServiceplanbundle(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    display_order = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment = models.ForeignKey(AttachmentsAttachment, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    service_plan = models.ForeignKey(ServicesServiceplan, models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_planbundle")

    class Meta:
        managed = False
        db_table = 'services_serviceplanbundle'


class ServicesServiceplanbundleHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    display_order = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    service_plan_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_serviceplanbundle_history'


class ServicesServiceplanpricing(models.Model):
    id = models.BigAutoField(primary_key=True)
    actual_price = models.DecimalField(max_digits=15, decimal_places=3)
    discounted_price = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    duration = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(GenericsCountrycurrency, models.DO_NOTHING)
    service_plan = models.ForeignKey(ServicesServiceplan, models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_planpricing")
    user_country = models.ForeignKey(GenericsCountry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'services_serviceplanpricing'


class ServicesServiceplanpricingHistory(models.Model):
    id = models.BigIntegerField()
    actual_price = models.DecimalField(max_digits=15, decimal_places=3)
    discounted_price = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    duration = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    service_plan_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_country_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_serviceplanpricing_history'


class ServicesUserserviceplan(models.Model):
    id = models.BigAutoField(primary_key=True)
    pos_unit_price = models.DecimalField(max_digits=15, decimal_places=3)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    payment_frequency = models.ForeignKey(ListOfValuesListofvalue, models.DO_NOTHING)
    payment_transaction = models.ForeignKey(AccountsPaymenttransaction, models.DO_NOTHING, blank=True, null=True)
    service_plan_pricing = models.ForeignKey(ServicesServiceplanpricing, models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_plan")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="user_plan")

    class Meta:
        managed = False
        db_table = 'services_userserviceplan'


class ServicesUserserviceplanHistory(models.Model):
    id = models.BigIntegerField()
    pos_unit_price = models.DecimalField(max_digits=15, decimal_places=3)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    payment_frequency_id = models.BigIntegerField(blank=True, null=True)
    payment_transaction_id = models.BigIntegerField(blank=True, null=True)
    service_plan_pricing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_userserviceplan_history'


class ServicesUservaluebundle(models.Model):
    id = models.BigAutoField(primary_key=True)
    pos_unit_price = models.DecimalField(max_digits=15, decimal_places=3)
    expiry_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    payment_transaction = models.ForeignKey(AccountsPaymenttransaction, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_bundle")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="user_services")
    value_bundle_pricing = models.ForeignKey('ServicesValuebundlepricing', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'services_uservaluebundle'


class ServicesUservaluebundleHistory(models.Model):
    id = models.BigIntegerField()
    pos_unit_price = models.DecimalField(max_digits=15, decimal_places=3)
    expiry_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    payment_transaction_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    value_bundle_pricing_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_uservaluebundle_history'


class ServicesValuebundle(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    display_order = models.IntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment = models.ForeignKey(AttachmentsAttachment, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_value")

    class Meta:
        managed = False
        db_table = 'services_valuebundle'


class ServicesValuebundleHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    display_order = models.IntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_valuebundle_history'


class ServicesValuebundleitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    display_order = models.IntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    service_item_category = models.ForeignKey(ListOfValuesListofvalue, models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_services")
    value_bundle = models.ForeignKey(ServicesValuebundle, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'services_valuebundleitem'


class ServicesValuebundleitemHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    display_order = models.IntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    service_item_category_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    value_bundle_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_valuebundleitem_history'


class ServicesValuebundlepricing(models.Model):
    id = models.BigAutoField(primary_key=True)
    bundle_price = models.DecimalField(max_digits=15, decimal_places=3)
    discounted_price = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    validity = models.IntegerField()
    is_region_dependent = models.BooleanField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_role = models.CharField(max_length=255, blank=True, null=True)
    asset_city = models.ForeignKey(GenericsCity, models.DO_NOTHING, blank=True, null=True)
    asset_country = models.ForeignKey(GenericsCountry, models.DO_NOTHING)
    asset_group = models.ForeignKey(AssetsAssetgroup, models.DO_NOTHING)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(GenericsCountrycurrency, models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_pricing")
    value_bundle = models.ForeignKey(ServicesValuebundle, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'services_valuebundlepricing'


class ServicesValuebundlepricingHistory(models.Model):
    id = models.BigIntegerField()
    bundle_price = models.DecimalField(max_digits=15, decimal_places=3)
    discounted_price = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    validity = models.IntegerField()
    is_region_dependent = models.BooleanField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_role = models.CharField(max_length=255, blank=True, null=True)
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_city_id = models.IntegerField(blank=True, null=True)
    asset_country_id = models.IntegerField(blank=True, null=True)
    asset_group_id = models.IntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    value_bundle_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_valuebundlepricing_history'


class UsersMarkettrend(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=200)
    total_visits = models.IntegerField()
    expire_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment = models.ForeignKey(AttachmentsAttachment, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('UsersUser', models.DO_NOTHING)
    updated_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_trend")

    class Meta:
        managed = False
        db_table = 'users_markettrend'


class UsersMarkettrendHistory(models.Model):
    id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=200)
    total_visits = models.IntegerField()
    expire_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_markettrend_history'


class UsersSocialloginprovider(models.Model):
    provider = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_socialloginprovider'


class UsersSocialloginproviderHistory(models.Model):
    id = models.IntegerField()
    provider = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_socialloginprovider_history'


class UsersSocialloginsetting(models.Model):
    client_id = models.TextField()
    client_secret = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    social_login_provider = models.OneToOneField(UsersSocialloginprovider, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_socialloginsetting'


class UsersSocialloginsettingHistory(models.Model):
    id = models.IntegerField()
    client_id = models.TextField()
    client_secret = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    social_login_provider_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_socialloginsetting_history'


class UsersUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=254)
    phone_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    social_image_url = models.CharField(max_length=200)
    referral_code = models.CharField(unique=True, max_length=10)
    blacklisted_reason = models.CharField(max_length=255)
    other_profession = models.CharField(max_length=50)
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=20)
    emergency_contact_phone_code = models.CharField(max_length=10)
    emergency_contact_email = models.CharField(max_length=254)
    email_verified = models.BooleanField()
    is_verified = models.BooleanField()
    is_blacklisted = models.BooleanField()
    last_logout = models.DateTimeField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    verified_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    profile_picture = models.ForeignKey(AttachmentsAttachment, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_user'
        unique_together = (('phone_code', 'phone_number'),)


class UsersUserGroups(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserHistory(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    id = models.BigIntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    phone_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    social_image_url = models.CharField(max_length=200)
    referral_code = models.CharField(max_length=10)
    blacklisted_reason = models.CharField(max_length=255)
    other_profession = models.CharField(max_length=50)
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=20)
    emergency_contact_phone_code = models.CharField(max_length=10)
    emergency_contact_email = models.CharField(max_length=254)
    email_verified = models.BooleanField()
    is_verified = models.BooleanField()
    is_blacklisted = models.BooleanField()
    last_logout = models.DateTimeField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    verified_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    profile_picture_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_user_history'


class UsersUserUserPermissions(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)


class UsersUseraddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=15)
    is_primary = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="user_created_by")
    location = models.ForeignKey(GenericsLocation, models.DO_NOTHING)
    updated_by = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_address")
    user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="user_address")

    class Meta:
        managed = False
        db_table = 'users_useraddress'


class UsersUseraddressHistory(models.Model):
    id = models.BigIntegerField()
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=15)
    is_primary = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    location_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_useraddress_history'


class UsersUseremployer(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    work_email = models.CharField(unique=True, max_length=254)
    work_employee_id = models.CharField(max_length=255)
    email_verified = models.BooleanField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    company = models.ForeignKey(GenericsCompany, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="employer_created_by")
    updated_by = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_employer")
    user = models.OneToOneField(UsersUser, models.DO_NOTHING, related_name="user_employer")

    class Meta:
        managed = False
        db_table = 'users_useremployer'


class UsersUseremployerHistory(models.Model):
    id = models.BigIntegerField()
    company_name = models.CharField(max_length=255)
    work_email = models.CharField(max_length=254)
    work_employee_id = models.CharField(max_length=255)
    email_verified = models.BooleanField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    company_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_useremployer_history'


class UsersUseridentitydocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_default = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment = models.ForeignKey(AttachmentsAttachment, models.DO_NOTHING)
    selfie_attachment = models.ForeignKey(AttachmentsAttachment, models.DO_NOTHING, related_name="attachment")
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_useridentitydocument'


class UsersUseridentitydocumentHistory(models.Model):
    id = models.BigIntegerField()
    is_default = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    selfie_attachment_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_useridentitydocument_history'


class UsersUserpreference(models.Model):
    id = models.BigAutoField(primary_key=True)
    metric_unit = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(UsersUser, models.DO_NOTHING)
    financial_year = models.ForeignKey(ListOfValuesListofvalue, models.DO_NOTHING, blank=True, null=True)
    locale = models.ForeignKey(ListOfValuesListofvalue, models.DO_NOTHING, blank=True, null=True, related_name="locale")
    updated_by = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True, related_name="updated_by_user_preference")
    user = models.OneToOneField(UsersUser, models.DO_NOTHING, related_name="user_preference")
    user_currency = models.ForeignKey(GenericsCountrycurrency, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_userpreference'


class UsersUserpreferenceHistory(models.Model):
    id = models.BigIntegerField()
    metric_unit = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    financial_year_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    locale_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    user_currency_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_userpreference_history'


class UsersUserreferralpoint(models.Model):
    id = models.BigAutoField(primary_key=True)
    referral_date = models.DateTimeField()
    points_received = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    referral_user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="user_referral")

    class Meta:
        managed = False
        db_table = 'users_userreferralpoint'


class UsersUserreferralpointHistory(models.Model):
    id = models.BigIntegerField()
    referral_date = models.DateTimeField()
    points_received = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    referral_user_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_userreferralpoint_history'


class UsersUserwithdrawal(models.Model):
    id = models.BigAutoField(primary_key=True)
    withdrawn_points = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_userwithdrawal'


class UsersUserwithdrawalHistory(models.Model):
    id = models.BigIntegerField()
    withdrawn_points = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_userwithdrawal_history'


class WorklistsTicket(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    created_by = models.ForeignKey(UsersUser, models.DO_NOTHING)
    lease_transaction = models.ForeignKey(AssetsLeasetransaction, models.DO_NOTHING, blank=True, null=True)
    raised_by = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="raised_by_user")
    ticket_category = models.ForeignKey(ListOfValuesListofvalue, models.DO_NOTHING)
    updated_by = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True, related_name="updated_by")

    class Meta:
        managed = False
        db_table = 'worklists_ticket'


class WorklistsTicketHistory(models.Model):
    id = models.BigIntegerField()
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    raised_by_id = models.BigIntegerField(blank=True, null=True)
    ticket_category_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worklists_ticket_history'
