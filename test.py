import product_pb2

p = product_pb2.Product(id=1, name="Ноут", price=21312.3)

print(p)

binary_data = p.SerializeToString()
print(len(binary_data))

restored = product_pb2.Product()
restored.ParseFromString(binary_data)

print(restored)