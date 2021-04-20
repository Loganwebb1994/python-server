SELECT
    c.id,
    c.email,
    c.name
FROM customer c
WHERE c.id = 2


INSERT INTO `Animal` VALUES (null, "Daps", "Kennel", "Boxer", 2, 2);

SELECT
    a.name,
    a.breed,
    a.status,
    a.location_id,            a.id,

    a.customer_id,
    l.name location_name,
    l.address location_address,
    c.email customer_email,
    c.name customer_name,
    c.address customer_address,
    c.password customer_password
FROM Animal a
JOIN Location l
    ON l.id = a.location_id
JOIN customer c 
    ON c.id = a.customer_id


SELECT * FROM animal ORDER BY id DESC;
