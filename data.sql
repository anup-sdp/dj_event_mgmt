--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5
-- Dumped by pg_dump version 17.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_group VALUES (2, 'Admin');
INSERT INTO public.auth_group VALUES (3, 'Organizer');
INSERT INTO public.auth_group VALUES (1, 'Participant');


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_content_type VALUES (1, 'admin', 'logentry');
INSERT INTO public.django_content_type VALUES (2, 'auth', 'permission');
INSERT INTO public.django_content_type VALUES (3, 'auth', 'group');
INSERT INTO public.django_content_type VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO public.django_content_type VALUES (5, 'sessions', 'session');
INSERT INTO public.django_content_type VALUES (6, 'core', 'category');
INSERT INTO public.django_content_type VALUES (7, 'core', 'event');
INSERT INTO public.django_content_type VALUES (8, 'users', 'customuser');


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_permission VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO public.auth_permission VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO public.auth_permission VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO public.auth_permission VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO public.auth_permission VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO public.auth_permission VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO public.auth_permission VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO public.auth_permission VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO public.auth_permission VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO public.auth_permission VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO public.auth_permission VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO public.auth_permission VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO public.auth_permission VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO public.auth_permission VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO public.auth_permission VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO public.auth_permission VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO public.auth_permission VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO public.auth_permission VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO public.auth_permission VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO public.auth_permission VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO public.auth_permission VALUES (21, 'Can add category', 6, 'add_category');
INSERT INTO public.auth_permission VALUES (22, 'Can change category', 6, 'change_category');
INSERT INTO public.auth_permission VALUES (23, 'Can delete category', 6, 'delete_category');
INSERT INTO public.auth_permission VALUES (24, 'Can view category', 6, 'view_category');
INSERT INTO public.auth_permission VALUES (25, 'Can add event', 7, 'add_event');
INSERT INTO public.auth_permission VALUES (26, 'Can change event', 7, 'change_event');
INSERT INTO public.auth_permission VALUES (27, 'Can delete event', 7, 'delete_event');
INSERT INTO public.auth_permission VALUES (28, 'Can view event', 7, 'view_event');
INSERT INTO public.auth_permission VALUES (29, 'Can add user', 8, 'add_customuser');
INSERT INTO public.auth_permission VALUES (30, 'Can change user', 8, 'change_customuser');
INSERT INTO public.auth_permission VALUES (31, 'Can delete user', 8, 'delete_customuser');
INSERT INTO public.auth_permission VALUES (32, 'Can view user', 8, 'view_customuser');


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_group_permissions VALUES (1, 2, 1);
INSERT INTO public.auth_group_permissions VALUES (2, 2, 2);
INSERT INTO public.auth_group_permissions VALUES (3, 2, 3);
INSERT INTO public.auth_group_permissions VALUES (4, 2, 4);
INSERT INTO public.auth_group_permissions VALUES (5, 2, 5);
INSERT INTO public.auth_group_permissions VALUES (6, 2, 6);
INSERT INTO public.auth_group_permissions VALUES (7, 2, 7);
INSERT INTO public.auth_group_permissions VALUES (8, 2, 8);
INSERT INTO public.auth_group_permissions VALUES (9, 2, 9);
INSERT INTO public.auth_group_permissions VALUES (10, 2, 10);
INSERT INTO public.auth_group_permissions VALUES (11, 2, 11);
INSERT INTO public.auth_group_permissions VALUES (12, 2, 12);
INSERT INTO public.auth_group_permissions VALUES (13, 2, 13);
INSERT INTO public.auth_group_permissions VALUES (14, 2, 14);
INSERT INTO public.auth_group_permissions VALUES (15, 2, 15);
INSERT INTO public.auth_group_permissions VALUES (16, 2, 16);
INSERT INTO public.auth_group_permissions VALUES (17, 2, 17);
INSERT INTO public.auth_group_permissions VALUES (18, 2, 18);
INSERT INTO public.auth_group_permissions VALUES (19, 2, 19);
INSERT INTO public.auth_group_permissions VALUES (20, 2, 20);
INSERT INTO public.auth_group_permissions VALUES (21, 2, 21);
INSERT INTO public.auth_group_permissions VALUES (22, 2, 22);
INSERT INTO public.auth_group_permissions VALUES (23, 2, 23);
INSERT INTO public.auth_group_permissions VALUES (24, 2, 24);
INSERT INTO public.auth_group_permissions VALUES (25, 2, 25);
INSERT INTO public.auth_group_permissions VALUES (26, 2, 26);
INSERT INTO public.auth_group_permissions VALUES (27, 2, 27);
INSERT INTO public.auth_group_permissions VALUES (28, 2, 28);
INSERT INTO public.auth_group_permissions VALUES (29, 2, 29);
INSERT INTO public.auth_group_permissions VALUES (30, 2, 30);
INSERT INTO public.auth_group_permissions VALUES (31, 2, 31);
INSERT INTO public.auth_group_permissions VALUES (32, 2, 32);
INSERT INTO public.auth_group_permissions VALUES (33, 3, 21);
INSERT INTO public.auth_group_permissions VALUES (34, 3, 22);
INSERT INTO public.auth_group_permissions VALUES (35, 3, 23);
INSERT INTO public.auth_group_permissions VALUES (36, 3, 24);
INSERT INTO public.auth_group_permissions VALUES (37, 3, 25);
INSERT INTO public.auth_group_permissions VALUES (38, 3, 26);
INSERT INTO public.auth_group_permissions VALUES (39, 3, 27);
INSERT INTO public.auth_group_permissions VALUES (40, 3, 28);
INSERT INTO public.auth_group_permissions VALUES (41, 1, 24);
INSERT INTO public.auth_group_permissions VALUES (42, 1, 32);
INSERT INTO public.auth_group_permissions VALUES (43, 1, 28);


--
-- Data for Name: core_category; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.core_category VALUES (1, 'Category 1', 'description of category 1');
INSERT INTO public.core_category VALUES (2, 'Category 2', 'Lorem ipsum dolor sit amet consectetur adipisicing elit.');
INSERT INTO public.core_category VALUES (3, 'Travel', 'travel for enjoyment');


--
-- Data for Name: core_event; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.core_event VALUES (1, 'Event 1', 'first event', '2025-07-25', '10:00:00', 'dhaka', 'image/upload/v1752723969/events_midterm/hn4jh15jmjqdxomad6zf.png', 1);
INSERT INTO public.core_event VALUES (2, 'event 2', 'description', '2025-09-14', '17:00:00', 'chittagong', 'image/upload/events_midterm/default_jb8jxq.png', 2);
INSERT INTO public.core_event VALUES (3, 'sundarban tour', 'cholo jai sundarban', '2025-12-31', '09:00:00', 'sundarban', 'image/upload/v1752724169/events_midterm/slghea2ohd46lte4fe0j.jpg', 3);


--
-- Data for Name: users_customuser; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users_customuser VALUES (3, 'pbkdf2_sha256$1000000$xuCGj21li4zLPkly4998Tl$6m0Ot/7e963cjuTsBqQpAukn+dDkQy+oQ1Zjvo+bXAk=', '2025-07-17 22:44:37.803859+06', false, 'pesam', 'pe', 'sam', 'pesam72345@lhory.com', false, true, '2025-07-16 11:30:18.81235+06', 'image/upload/v1752693323/profile_images/iy4qhzdwgiyc8o8ba6as.jpg', 'hi i am pesam.', NULL);
INSERT INTO public.users_customuser VALUES (4, 'pbkdf2_sha256$1000000$dwnn8tkxhkDyDQPi3SMuTT$kCdbhcR4Bfr8cdvo+SGC12Wk9c/0Zbt3EU/oqNs4hew=', '2025-07-18 01:47:58.788531+06', false, 'getekiy', 'get', 'ekiy', 'getekiy737@hosintoy.com', false, true, '2025-07-18 01:47:14.914177+06', 'image/upload/profile_images/default_img.png', NULL, NULL);
INSERT INTO public.users_customuser VALUES (1, 'pbkdf2_sha256$1000000$hsDD07ng7ykthCbrQyrv74$YoDV4HirhsRtlpVxiL0VF0Z2U6pvqZ3WrBt1Fb6TWeA=', '2025-07-18 01:49:12.892173+06', true, 'admin', 'Admin', 'Mohasoy', 'admin@example.com', true, true, '2025-07-16 10:16:49.897119+06', 'image/upload/v1752644248/profile_images/fa9510lzr15amiao86ro.png', 'born to be admin', NULL);
INSERT INTO public.users_customuser VALUES (2, 'pbkdf2_sha256$1000000$xohTayffdntI7dEvdMXfDl$pehiynJk9MsQAPbxAdq9r9atcdWasZ3bzJ/9CZEbUaI=', '2025-07-17 09:34:24.163402+06', true, 'anup', 'Anup', 'Barua', 'anupbarua30@gmail.com', true, true, '2025-07-16 10:40:18.947951+06', 'image/upload/v1752644561/profile_images/yrmaecdxvpt97csinxqw.jpg', 'i am a passionate web developer.', '01913378482');


--
-- Data for Name: core_event_participants; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.core_event_participants VALUES (1, 1, 2);
INSERT INTO public.core_event_participants VALUES (2, 1, 3);
INSERT INTO public.core_event_participants VALUES (3, 3, 4);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_admin_log VALUES (1, '2025-07-16 11:13:44.47311+06', '2', 'Admin', 1, '[{"added": {}}]', 3, 1);
INSERT INTO public.django_admin_log VALUES (2, '2025-07-16 11:16:19.643744+06', '3', 'Organizer', 1, '[{"added": {}}]', 3, 1);
INSERT INTO public.django_admin_log VALUES (3, '2025-07-16 11:17:37.242712+06', '1', 'Participant', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 1);
INSERT INTO public.django_admin_log VALUES (4, '2025-07-16 11:35:09.209121+06', '2', 'anup', 2, '[{"changed": {"fields": ["Groups"]}}]', 8, 1);
INSERT INTO public.django_admin_log VALUES (5, '2025-07-16 11:37:28.968096+06', '1', 'admin', 2, '[{"changed": {"fields": ["First name", "Last name", "Bio", "Image"]}}]', 8, 1);
INSERT INTO public.django_admin_log VALUES (6, '2025-07-16 11:42:42.214133+06', '2', 'anup', 2, '[{"changed": {"fields": ["First name", "Last name", "Bio", "Image"]}}]', 8, 1);
INSERT INTO public.django_admin_log VALUES (7, '2025-07-17 06:53:46.058933+06', '1', 'admin', 2, '[{"changed": {"fields": ["Groups"]}}]', 8, 1);
INSERT INTO public.django_admin_log VALUES (8, '2025-07-17 06:53:54.316881+06', '2', 'anup', 2, '[]', 8, 1);
INSERT INTO public.django_admin_log VALUES (9, '2025-07-17 06:54:01.741264+06', '3', 'pesam', 2, '[]', 8, 1);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_migrations VALUES (1, 'contenttypes', '0001_initial', '2025-07-16 10:15:22.89318+06');
INSERT INTO public.django_migrations VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2025-07-16 10:15:22.897179+06');
INSERT INTO public.django_migrations VALUES (3, 'auth', '0001_initial', '2025-07-16 10:15:22.924191+06');
INSERT INTO public.django_migrations VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2025-07-16 10:15:22.927191+06');
INSERT INTO public.django_migrations VALUES (5, 'auth', '0003_alter_user_email_max_length', '2025-07-16 10:15:22.930192+06');
INSERT INTO public.django_migrations VALUES (6, 'auth', '0004_alter_user_username_opts', '2025-07-16 10:15:22.933193+06');
INSERT INTO public.django_migrations VALUES (7, 'auth', '0005_alter_user_last_login_null', '2025-07-16 10:15:22.936192+06');
INSERT INTO public.django_migrations VALUES (8, 'auth', '0006_require_contenttypes_0002', '2025-07-16 10:15:22.938192+06');
INSERT INTO public.django_migrations VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2025-07-16 10:15:22.941192+06');
INSERT INTO public.django_migrations VALUES (10, 'auth', '0008_alter_user_username_max_length', '2025-07-16 10:15:22.944192+06');
INSERT INTO public.django_migrations VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2025-07-16 10:15:22.947192+06');
INSERT INTO public.django_migrations VALUES (12, 'auth', '0010_alter_group_name_max_length', '2025-07-16 10:15:22.952192+06');
INSERT INTO public.django_migrations VALUES (13, 'auth', '0011_update_proxy_permissions', '2025-07-16 10:15:22.956192+06');
INSERT INTO public.django_migrations VALUES (14, 'auth', '0012_alter_user_first_name_max_length', '2025-07-16 10:15:22.959192+06');
INSERT INTO public.django_migrations VALUES (15, 'users', '0001_initial', '2025-07-16 10:15:22.982929+06');
INSERT INTO public.django_migrations VALUES (16, 'admin', '0001_initial', '2025-07-16 10:15:22.996709+06');
INSERT INTO public.django_migrations VALUES (17, 'admin', '0002_logentry_remove_auto_add', '2025-07-16 10:15:23.000709+06');
INSERT INTO public.django_migrations VALUES (18, 'admin', '0003_logentry_add_action_flag_choices', '2025-07-16 10:15:23.005708+06');
INSERT INTO public.django_migrations VALUES (19, 'core', '0001_initial', '2025-07-16 10:15:23.029075+06');
INSERT INTO public.django_migrations VALUES (20, 'sessions', '0001_initial', '2025-07-16 10:15:23.036925+06');
INSERT INTO public.django_migrations VALUES (21, 'users', '0002_customuser_phone_number', '2025-07-17 06:41:46.698288+06');
INSERT INTO public.django_migrations VALUES (22, 'users', '0003_alter_customuser_profile_image', '2025-07-17 07:33:19.286693+06');


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_session VALUES ('fal770jy9bztcume4n0sp8cvulb3l4cm', '.eJxVjEEOwiAQRe_C2hBKhQGX7nsGMsOAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnERgzj9boTxkeoO-I711mRsdV1mkrsiD9rl1Dg9r4f7d1Cwl2-tgRwkhJystqT8yBqsYuQBMjums7PZjOzUqMggeTA5GaM0R2AgH8X7A-sxOEM:1ubumq:ujqtq0TRgck08i7Hghv4GNEiwjys4E17DSARUwk_yB8', '2025-07-30 11:34:36.125723+06');
INSERT INTO public.django_session VALUES ('1ihanwpwt6ly5jp47mfd1pq72ckpk0od', '.eJxVjMsOwiAQAP-FsyHLS1iP3v0GssBiq4YmpT0Z_92Q9KDXmcm8RaR9m-LeeY1zERehxemXJcpPbkOUB7X7IvPStnVOciTysF3elsKv69H-DSbq09ii0kjkUXNwrJMBg8W4QHgGtuQt1ErVOkSGqpzPCsB4pTNwLkEp8fkCw583DA:1ucDNh:9imw-NjC3K1SK1Rizvb3ekr38x2gQBpefY_-tfxezcs', '2025-07-31 07:25:53.462583+06');
INSERT INTO public.django_session VALUES ('nufx2oxxjxz6vm7e5tdvxoy23nhg3ntc', '.eJxVjDsOwjAQRO_iGlnZsKxjSvqcIdr1BweQLcVJhbg7sZQCynnzZt5q4m1N01bDMs1eXdVZnX6ZsHuG3Ar_4Hwv2pW8LrPopuijrXosPrxuh_t3kLimtgZC6Qk8kzOdYd7zwBh5xxjBuoux7EUQ0UmQzlihwUPskRgASX2-6pU38w:1ucRLh:mN3B_E6W3rFTX46ZbbX-QFlhAt4ODPuq43q66hHnxvM', '2025-07-31 22:20:45.1452+06');
INSERT INTO public.django_session VALUES ('to3sjxpmn2bjyyw3as10ccbuu5goz8c3', '.eJxVjEEOwiAQRe_C2hBKhQGX7nsGMsOAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnERgzj9boTxkeoO-I711mRsdV1mkrsiD9rl1Dg9r4f7d1Cwl2-tgRwkhJystqT8yBqsYuQBMjums7PZjOzUqMggeTA5GaM0R2AgH8X7A-sxOEM:1ucUbQ:izZ7AO7uazHcIcQt4qC7fDzsMvggLthHG0Zoyc0LB1Y', '2025-08-01 01:49:12.894381+06');


--
-- Data for Name: users_customuser_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users_customuser_groups VALUES (4, 2, 3);
INSERT INTO public.users_customuser_groups VALUES (5, 1, 2);
INSERT INTO public.users_customuser_groups VALUES (7, 3, 1);
INSERT INTO public.users_customuser_groups VALUES (8, 4, 1);


--
-- Data for Name: users_customuser_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 3, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 43, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 32, true);


--
-- Name: core_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_category_id_seq', 4, true);


--
-- Name: core_event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_event_id_seq', 3, true);


--
-- Name: core_event_participants_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_event_participants_id_seq', 3, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 9, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 8, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 22, true);


--
-- Name: users_customuser_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_customuser_groups_id_seq', 8, true);


--
-- Name: users_customuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_customuser_id_seq', 4, true);


--
-- Name: users_customuser_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_customuser_user_permissions_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

