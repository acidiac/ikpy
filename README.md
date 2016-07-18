Indigenous Knowledge Network
Web Platform
version 0.0.2
Backend API built on python flask

Author: Amit Chanchal, amit.chanchal@hotmail.com

some references to look at --->
creating beautiful rest apis with flask (http://pycoder.net/bospy/presentation.html#cuc-8)
designing restful API, Miguel Grinberg (http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)

======================================
Version 0.0.2 design Specification
======================================
KEY MODULES:
-> users : <@access>user</@access> Manage all the users functionality 
	#authentication, profile_admin, user_log, user_relations[organization, IK, communities], activity logger, api_calls, logins
	-> Roles and access control

-> Organisation : <@acess>Admin User</@acess>  Manages the main dataset for the organization
	# creates an admin role for a user, also allows other users to be linked to the organization pending the approval of the admin. Check admin url to be same as the main url or if otherwise mentioned, Also allows institution to create content which can be published then by the organization. maybe then the admin level access and fcuntionality have to have great level of control and managerial tools.
	-> add/remove/update roles, add/remove/update users, add/remove/update events, manage publication, notifications and others 

-> IK : <@access>All users verification by admin users</@access> Manage list of documented Indigenous knowledge, these can be added by anyone and once approved would be commited to the database.
	-> add/suggest IK, Edit IK, Add communities/organizations/person

-> Communities : <@access>All user and verification by admin users</@access> these can be suggested by users and organizations and will be commited to the database after varification by the network admin.
	-> add/suggest IK, Edit IK, Add IK/organizations/person

-> Events- <@access> Network admin, Org Admin, Community Admin</@access>
	-> Create events, notification, registration, pricing, other details

-> Resources- <@access>Admin user only</@access>

-> Blogs and Media <@access>Respective Roles</@access>



	



