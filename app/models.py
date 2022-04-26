from django.db import models

# Create your models here.
class Outlet(models.Model):
    outletID =   models.CharField(max_length = 200, primary_key= True)     #int
    outletName = models.CharField(max_length = 200)   #varchar(20)
    area = models.CharField(max_length = 200)         #varchar(20)
    city = models.CharField(max_length = 200)         #varchar(20)
    state = models.CharField(max_length = 50)        #varchar(20)
    pincode = models.CharField(max_length = 20)      #int/varchar(20)

    def __str__(self): 
        return self.outletName

class Waiter(models.Model):
    waiterID = models.CharField(max_length = 200, primary_key= True)     #int
    firstName = models.CharField(max_length = 200)    #varchar(20)
    lastName = models.CharField(max_length = 200)     #varchar(20)
    #waiterRating =  int/float
    outletID = models.ForeignKey(Outlet, on_delete = models.CASCADE)     #int

    def __str__(self): 
        return self.firstName


class CustomerInfo(models.Model):
    customerID = models.AutoField(primary_key= True)                                     #int
    customerName = models.CharField(max_length = 200)                   #varchar
    customerPhone = models.CharField(max_length = 20)                   #int/varchar
    registrationDate = models.DateField(auto_now = True)                #date
    walletMoney = models.FloatField()                                   #float
    waiterID = models.ForeignKey(Waiter, on_delete = models.CASCADE)    #int
    def __str__(self): 
        return self.customerName

class Bill(models.Model):
    orderID = models.AutoField(primary_key= True)
    customerID = models.ForeignKey(CustomerInfo, on_delete = models.CASCADE)   #int
    orderWaiter = models.ForeignKey(Waiter, on_delete = models.CASCADE)  #int, get waiterID
    orderDate = models.DateField(auto_now = True)    #date

    @property
    def customerName(self):
        return self.customerID.customerName
    
    @property
    def customerPhone(self):
        return self.customerID.customerPhone

    @property
    def cost(self):
        it_quant = Creates.objects.filter(orderID = self.orderID).values('itemID', 'itemQty')
        #for i in it_quant:
         #   id = it_quant.get('itemID')
        #    k = ItemDetails.filter(itemID = id).values('itemPrice','itemName')
        #    i.update(k)
         #   cost = i.get('itemQty') * i.get('itemPrice')
          #  i['costPerItem'] = cost
           # print(it_quant)
        return it_quant
        

    class Meta:
        unique_together = (("orderID" , "customerID"))


class OutletPhone(models.Model):
    outletID = models.ForeignKey(Outlet, on_delete = models.CASCADE,)     #int
    phoneNo = models.CharField(max_length = 10)
    
    class Meta: 
        unique_together = (("outletID", "phoneNo"))     #int/varchar

class WaiterOrderID(models.Model):
    waiterID = models.ForeignKey(Waiter, on_delete = models.CASCADE,)        #int
    orderID =  models.ForeignKey(Bill, on_delete = models.CASCADE, )  #int

    class Meta: 
        unique_together = (("waiterID", "orderID"))

class ItemDetails(models.Model):
    itemID = models.AutoField(primary_key=True)           #int
    itemName = models.CharField(max_length = 200)        # varchar(20)
    itemPrice = models.FloatField()        #int
    itemDescription = models.CharField(max_length = 200) #varchar(200)
    itemSize = models.BigIntegerField()         #int
    outletID = models.ForeignKey(Outlet, on_delete = models.CASCADE);        #add

    def __str__(self): 
        return self.itemName


class Inventory(models.Model):
    materialID = models.AutoField(primary_key= True)      #int
    materialQty = models.FloatField()    #int
    materialName = models.CharField(max_length = 200)     #varchar(20)
    threshQty = models.FloatField()      #int
    costPrice = models.FloatField()      #int/float
    orderedStatus = models.BigIntegerField() #int

    def __str__(self): 
        return self.materialName

class InventoryDistributor(models.Model):
    materialID = models.ForeignKey(Inventory, on_delete = models.CASCADE, )      #int
    distributorName = models.CharField(max_length = 200 )  #varchar(20)

    class Meta:
        unique_together = (("materialID", "distributorName"))

class Creates(models.Model):
    #customerID = models.ForeignKey(CustomerInfo, on_delete = models.CASCADE, )      #int
    orderID = models.ForeignKey(Bill, models.CASCADE)         #int
    itemID =  models.ForeignKey(ItemDetails, on_delete = models.CASCADE, )       #int
    itemQty = models.BigIntegerField()         #int

    @property
    def itemName(self):
        return self.itemID.itemName

    @property
    def itemPrice(self):
        return self.itemID.itemPrice

    @property
    def costPerItem(self):
        return self.itemQty * self.itemPrice

    class Meta:
        unique_together = (( "orderID", "itemID"))

