SELECT pk_id_productos,nombre,existencia,valor_compra,valor_por_mayor,valor_deltal 
FROM precios  
INNER JOIN productos ON productos.pk_id_productos=precios.fk_id_productos;

SELECT * FROM precios;