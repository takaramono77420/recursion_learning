class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class InvoiceItem:
    def __init__(self, product, quantity, next=None):
        self.product = product
        self.quantity = quantity
        self.next = next
    
    def getTotalPrice(self):
        return self.product.price * self.quantity

class Invoice:
    def __init__(self, invoiceNumber, invoiceItemHead=None):
        self.invoiceNumber = invoiceNumber
        self.invoiceItemHead = invoiceItemHead
    
    def amountDue(self, taxes):
        currentNode = self.invoiceItemHead
        output = 0
        while currentNode is not None:
            output += currentNode.getTotalPrice()
            currentNode = currentNode.next
        
        if taxes:
            output *= 1.1
        
        return output

product1 = Product("shampoo", 10)
product2 = Product("conditioner", 5)
product3 = Product("tooth brush", 3)

firstItem = InvoiceItem(product1, 7)
secondItem = InvoiceItem(product2, 9)
thirdItem = InvoiceItem(product3, 10)

firstItem.next = secondItem
secondItem.next = thirdItem
invoice = Invoice("UC1234567890", firstItem)


print(invoice.amountDue(False))
print(invoice.amountDue(True))

