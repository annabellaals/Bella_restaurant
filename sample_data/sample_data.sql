insert into home_foodtype (id, name, created_at, updated_at)
values  ('9f894e2725da484a98a99694a5a8b9e4', 'Burger', '2024-08-23 21:38:55.546916', '2024-08-23 21:38:55.546976'),
        ('e01e4e937dc0420b879fea9b3bdd6561', 'Pizza', '2024-08-23 21:38:58.898064', '2024-08-23 21:38:58.898115'),
        ('8a8c7ca3476f425a8301b7f6383c43c9', 'Pasta', '2024-08-23 21:39:02.020054', '2024-08-23 21:39:02.020110'),
        ('da82874209b84a9baeea3c3d464046e6', 'Fries', '2024-08-23 21:39:04.970888', '2024-08-23 21:39:04.970935'),
        ('2fefa163658847fea51e55d812e08e65', 'Dessert', '2024-08-24 17:07:29.399099', '2024-08-24 17:07:29.399150');

INSERT INTO home_food (id, name, image, description, price, available, created_at, updated_at, food_type_id)
VALUES
    ('b558c9efff354c48a7f270aeecdfdadf', 'Margherita Pizza', 'f1.png', 'Classic Margherita Pizza with fresh mozzarella, basil, and a rich tomato sauce on a crispy crust.', 20, true, '2024-08-23 21:39:57.356896', '2024-08-23 21:43:06.737609', 'e01e4e937dc0420b879fea9b3bdd6561'),
    ('d3f9fba0fbd84f47942f789b751a0b0e', 'Cheddar Cheeseburger', 'f2.png', 'Juicy beef patty topped with melted cheddar cheese, crisp lettuce, fresh tomato, and pickles, served on a toasted bun.', 15, true, '2024-08-23 21:43:39.249191', '2024-08-23 21:43:39.249237', '9f894e2725da484a98a99694a5a8b9e4'),
    ('ae6b215e3742453b8064a0ea83bd1eba', 'Pepperoni Pizza', 'f3.png', 'Spicy pepperoni slices on a bed of melted mozzarella cheese and tomato sauce, topped with oregano on a crispy crust.', 17, true, '2024-08-23 21:44:04.573950', '2024-08-23 21:44:04.573994', 'e01e4e937dc0420b879fea9b3bdd6561'),
    ('6bd16b9fe19946619c13d361dd33a1bb', 'Penne Alfredo', 'f4.png', 'Creamy Alfredo sauce over tender penne pasta, garnished with grated Parmesan and a touch of parsley.', 18, true, '2024-08-23 21:44:26.175331', '2024-08-23 21:44:29.255246', '8a8c7ca3476f425a8301b7f6383c43c9'),
    ('55c303e73e274ae58fd3a916af32ba65', 'Crispy French Fries', 'f5.png', 'Golden brown and crispy French fries, seasoned to perfection and served with your choice of dipping sauce.', 10, true, '2024-08-23 21:44:52.545502', '2024-08-23 21:44:52.545549', 'da82874209b84a9baeea3c3d464046e6'),
    ('9e7a86de8b334282ace4084198f07aa3', 'Vegetarian Margherita Pizza', 'f3_WiHyPjU.png', 'Fresh Margherita Pizza with a variety of garden vegetables including bell peppers, onions, and mushrooms on a crispy crust.', 15, true, '2024-08-23 21:45:17.594291', '2024-08-23 21:58:30.008854', 'e01e4e937dc0420b879fea9b3bdd6561'),
    ('72928c646eec4d2999d4e19c19db03a3', 'Spicy BBQ Bacon Burger', 'f7.png', 'Spicy BBQ Bacon Burger featuring a seasoned beef patty with crispy bacon, smoky BBQ sauce, and a hint.', 12, true, '2024-08-23 21:45:40.705418', '2024-08-23 21:45:40.705475', '9f894e2725da484a98a99694a5a8b9e4'),
    ('da30665b38ee495ab62a92c92c4872bd', 'Veggie Delight Burger', 'f8.png', 'A hearty veggie burger made from a blend of garden-fresh vegetables and grains, topped with avocado, lettuce, and tomato.', 14, true, '2024-08-23 21:46:02.771555', '2024-08-23 21:46:02.771602', '9f894e2725da484a98a99694a5a8b9e4'),
    ('03cd2df06e5744c284b7240a0be187c3', 'Spaghetti Carbonara', 'f9.png', 'Classic Spaghetti Carbonara with creamy sauce, pancetta, Parmesan cheese, and a touch of black pepper.', 10, true, '2024-08-23 21:46:25.772282', '2024-08-23 21:46:25.772327', '8a8c7ca3476f425a8301b7f6383c43c9'),
    ('9c588412f31a449ba94373604b624e50', 'Rich Chocolate Cake', 'client1_xk4ey5m.jpg', 'Decadent chocolate cake with layers of rich chocolate ganache and a moist, fudgy texture, topped with chocolate shavings.', 10, true, '2024-08-24 17:08:13.314646', '2024-08-24 17:08:13.314688', '2fefa163658847fea51e55d812e08e65');

insert into main.home_reservationtables (id, table_id, created_at, updated_at)
values  ('9410a20058a74ed4948b65ab4ddca5f5', 'Table A', '2024-08-30 17:21:14.220688', '2024-08-30 17:21:26.177152'),
        ('8f23caf264664ef991c689f30425179c', 'Table B', '2024-08-30 17:21:20.644211', '2024-08-30 17:21:20.644264'),
        ('391c32415c2b470caba1a1a6128e6dd7', 'Table C', '2024-08-30 17:21:32.349286', '2024-08-30 17:21:32.349336'),
        ('2c72db1db62d4f66b723c37c8f4bd10c', 'Table D', '2024-08-30 17:21:39.019014', '2024-08-30 17:21:39.019075'),
        ('7b57f93e063348fc9a1853655bea6563', 'Table E', '2024-08-30 17:21:43.643143', '2024-08-30 17:21:43.643222'),
        ('0c52da62c2b44d499a333ef08dd46353', 'Table F', '2024-08-30 17:21:48.513215', '2024-08-30 17:21:48.513256'),
        ('acf3660c740a4b47b8b4569296051b86', 'Table G', '2024-08-30 17:21:53.117728', '2024-08-30 17:21:53.117787'),
        ('8ccab965c4604fba993089ae517b6bed', 'Table H', '2024-08-30 17:21:58.203789', '2024-08-30 17:21:58.203847');