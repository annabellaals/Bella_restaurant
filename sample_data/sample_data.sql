insert into home_foodtype (id, name, created_at, updated_at)
values  ('9f894e2725da484a98a99694a5a8b9e4', 'Burger', '2024-08-23 21:38:55.546916', '2024-08-23 21:38:55.546976'),
        ('e01e4e937dc0420b879fea9b3bdd6561', 'Pizza', '2024-08-23 21:38:58.898064', '2024-08-23 21:38:58.898115'),
        ('8a8c7ca3476f425a8301b7f6383c43c9', 'Pasta', '2024-08-23 21:39:02.020054', '2024-08-23 21:39:02.020110'),
        ('da82874209b84a9baeea3c3d464046e6', 'Fries', '2024-08-23 21:39:04.970888', '2024-08-23 21:39:04.970935'),
        ('2fefa163658847fea51e55d812e08e65', 'Dessert', '2024-08-24 17:07:29.399099', '2024-08-24 17:07:29.399150');

insert into home_food (id, name, image, description, price, available, created_at, updated_at, food_type_id)
values  ('b558c9efff354c48a7f270aeecdfdadf', 'Delicious Pizza', 'f1.png', 'Veniam debitis quaerat officiis quasi cupiditate quo, quisquam velit, magnam voluptatem repellendus sed eaque', 20, true, '2024-08-23 21:39:57.356896', '2024-08-23 21:43:06.737609', 'e01e4e937dc0420b879fea9b3bdd6561'),
        ('d3f9fba0fbd84f47942f789b751a0b0e', 'Delicious Burger', 'f2.png', 'Juicy beef patty topped with melted cheddar cheese, crisp lettuce, fresh tomato, and pickles,', 15, true, '2024-08-23 21:43:39.249191', '2024-08-23 21:43:39.249237', '9f894e2725da484a98a99694a5a8b9e4'),
        ('ae6b215e3742453b8064a0ea83bd1eba', 'Delicious Pizza', 'f3.png', 'Veniam debitis quaerat officiis quasi cupiditate quo, quisquam velit, magnam voluptatem repellendus sed eaque', 17, true, '2024-08-23 21:44:04.573950', '2024-08-23 21:44:04.573994', 'e01e4e937dc0420b879fea9b3bdd6561'),
        ('6bd16b9fe19946619c13d361dd33a1bb', 'Delicious Pasta', 'f4.png', 'Veniam debitis quaerat officiis quasi cupiditate quo, quisquam velit, magnam voluptatem repellendus sed eaque', 18, true, '2024-08-23 21:44:26.175331', '2024-08-23 21:44:29.255246', '8a8c7ca3476f425a8301b7f6383c43c9'),
        ('55c303e73e274ae58fd3a916af32ba65', 'French Fries', 'f5.png', 'Veniam debitis quaerat officiis quasi cupiditate quo, quisquam velit, magnam voluptatem repellendus sed eaque', 10, true, '2024-08-23 21:44:52.545502', '2024-08-23 21:44:52.545549', 'da82874209b84a9baeea3c3d464046e6'),
        ('9e7a86de8b334282ace4084198f07aa3', 'Delicious Pizza', 'f3_WiHyPjU.png', 'Veniam debitis quaerat officiis quasi cupiditate quo, quisquam velit, magnam voluptatem repellendus sed eaque', 15, true, '2024-08-23 21:45:17.594291', '2024-08-23 21:58:30.008854', 'e01e4e937dc0420b879fea9b3bdd6561'),
        ('72928c646eec4d2999d4e19c19db03a3', 'Spicy BBQ Bacon Burger', 'f7.png', 'Savor the heat with our spicy BBQ bacon burger! A perfectly seasoned beef patty, smoky bacon, zesty BBQ sauce', 12, true, '2024-08-23 21:45:40.705418', '2024-08-23 21:45:40.705475', '9f894e2725da484a98a99694a5a8b9e4'),
        ('da30665b38ee495ab62a92c92c4872bd', 'Veggie Delight Burger', 'f8.png', 'Enjoy a wholesome veggie patty made with a blend of garden-fresh vegetables and grains, topped with avocado,', 14, true, '2024-08-23 21:46:02.771555', '2024-08-23 21:46:02.771602', '9f894e2725da484a98a99694a5a8b9e4'),
        ('03cd2df06e5744c284b7240a0be187c3', 'Delicious Pasta', 'f9.png', 'Veniam debitis quaerat officiis quasi cupiditate quo, quisquam velit, magnam voluptatem repellendus sed eaque', 10, true, '2024-08-23 21:46:25.772282', '2024-08-23 21:46:25.772327', '8a8c7ca3476f425a8301b7f6383c43c9'),
        ('9c588412f31a449ba94373604b624e50', 'Delicious Ice cream', 'client1_xk4ey5m.jpg', 'Veniam debitis quaerat officiis quasi cupiditate quo, quisquam velit, magnam voluptatem repellendus sed eaque', 10, true, '2024-08-24 17:08:13.314646', '2024-08-24 17:08:13.314688', '2fefa163658847fea51e55d812e08e65');