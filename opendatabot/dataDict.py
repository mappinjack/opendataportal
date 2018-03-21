
# Service directory: https://services.arcgis.com/ZpeBVw5o1kjit7LT/ArcGIS/rest/services

dataDict = {
	"parks" : {
		"endpoint": "https://services.arcgis.com/ZpeBVw5o1kjit7LT/arcgis/rest/services/ParksSpaces/FeatureServer/0/",
		"downloadUrls" : {"csv" : "https://opendata.arcgis.com/datasets/5934645858f24c06944352c0ce285b4e_0.csv",
						  "kml" : "https://opendata.arcgis.com/datasets/5934645858f24c06944352c0ce285b4e_0.kml",
						  "shp" : "https://opendata.arcgis.com/datasets/5934645858f24c06944352c0ce285b4e_0.zip",
						  "gdb" : "https://www.arcgis.com/sharing/rest/content/items/865f4c0497c7425a98ae13774b0c4b56/data"},
		"metaUrl" : "https://services.arcgis.com/ZpeBVw5o1kjit7LT/ArcGIS/rest/services/ParksSpaces/FeatureServer?f=pjson",
		"attributesUrl" : "https://services.arcgis.com/ZpeBVw5o1kjit7LT/arcgis/rest/services/ParksSpaces/FeatureServer/layers?f=json",
		"popupFields":["PARK_NAME"]},

	"buildings" : {
		"endpoint" : "https://services1.arcgis.com/qAo1OsXi67t7XgmS/arcgis/rest/services/Buildings/FeatureServer/0/",
		"downloadUrls" : {"csv" : "https://opendata.arcgis.com/datasets/f32d5f6f5fb54ced93ee47eb468bcc59_0.csv",
						  "kml" : "https://opendata.arcgis.com/datasets/f32d5f6f5fb54ced93ee47eb468bcc59_0.kml",
						  "shp" : "https://opendata.arcgis.com/datasets/f32d5f6f5fb54ced93ee47eb468bcc59_0.zip",
						  "gdb" : "https://www.arcgis.com/sharing/rest/content/items/71af995f90024ea7a5e8ba69d940599b/data"},
		"metaUrl" : "https://services1.arcgis.com/qAo1OsXi67t7XgmS/arcgis/rest/services/Buildings/FeatureServer?f=pjson",
		"attributesUrl" : "https://services1.arcgis.com/qAo1OsXi67t7XgmS/arcgis/rest/services/Buildings/FeatureServer/layers?f=pjson",
		"popupFields":["SUBCATEGORY", "STORIES"]},

	"trails" : {
		"endpoint" : "https://services.arcgis.com/ZpeBVw5o1kjit7LT/arcgis/rest/services/Trails/FeatureServer/0/",
		"downloadUrls" : {"csv" : "https://opendata.arcgis.com/datasets/09663cae662d4bba8b4fd4be11b6a69e_0.csv",
						  "kml" : "https://opendata.arcgis.com/datasets/09663cae662d4bba8b4fd4be11b6a69e_0.kml",
						  "shp" : "https://opendata.arcgis.com/datasets/09663cae662d4bba8b4fd4be11b6a69e_0.zip",
						  "gdb" : "https://www.arcgis.com/sharing/rest/content/items/76548391d1ca4c4b9d99bf692e995471/data"},
		"metaUrl" : "https://services.arcgis.com/ZpeBVw5o1kjit7LT/ArcGIS/rest/services/Trails/FeatureServer?f=pjson",
		"attributesUrl" : "https://services.arcgis.com/ZpeBVw5o1kjit7LT/ArcGIS/rest/services/Trails/FeatureServer/layers?f=pjson",
		"popupFields":["PATH_TYPE"]},

	"recreation points": {
		"endpoint": "https://services.arcgis.com/ZpeBVw5o1kjit7LT/arcgis/rest/services/RecreationPoints/FeatureServer/0/",
		"downloadUrls" : {"csv" : "https://opendata.arcgis.com/datasets/bf129a5294134d178fcd37857e2ab0fe_0.csv",
						  "kml" : "https://opendata.arcgis.com/datasets/bf129a5294134d178fcd37857e2ab0fe_0.kml",
						  "shp" : "https://opendata.arcgis.com/datasets/bf129a5294134d178fcd37857e2ab0fe_0.zip",
						  "gdb" : "https://www.arcgis.com/sharing/rest/content/items/5d57861e5aee47218d26a3fd1868bed4/data"},
		"metaUrl" : "https://services.arcgis.com/ZpeBVw5o1kjit7LT/ArcGIS/rest/services/RecreationPoints/FeatureServer?f=pjson",
		"attributesUrl" : "https://services.arcgis.com/ZpeBVw5o1kjit7LT/ArcGIS/rest/services/RecreationPoints/FeatureServer/layers?f=pjson",
	    "popupFields":["NAME","TYPE","ADDRESS"]},

	"creeks": {
		"endpoint": "https://services.arcgis.com/ZpeBVw5o1kjit7LT/arcgis/rest/services/WaterFeatures_Creeks/FeatureServer/0/",
		"downloadUrls" : {"csv" : "https://opendata.arcgis.com/datasets/8f47335389d44575bea09e5d8bf03e34_0.csv",
						  "kml" : "https://opendata.arcgis.com/datasets/8f47335389d44575bea09e5d8bf03e34_0.kml",
						  "shp" : "https://opendata.arcgis.com/datasets/8f47335389d44575bea09e5d8bf03e34_0.zip",
						  "gdb" : "https://www.arcgis.com/sharing/rest/content/items/f4e73c39ccc14e2ba8f21be637f26734/data"},
		"metaUrl" : "https://services.arcgis.com/ZpeBVw5o1kjit7LT/arcgis/rest/services/WaterFeatures_Creeks/FeatureServer?f=pjson",
		"attributesUrl" : "https://services.arcgis.com/ZpeBVw5o1kjit7LT/arcgis/rest/services/WaterFeatures_Creeks/FeatureServer/layers?f=pjson",
	    "popupFields":["NAME"]},
	"pWorship":{
	    "endpoint": "https://services.arcgis.com/ZpeBVw5o1kjit7LT/arcgis/rest/services/PlacesOfWorship/FeatureServer/0/",
	    "downloadUrls": {"csv": "https://opendata.arcgis.com/datasets/5d90eeb4db7d49ab99f0565ff612eb1c_0.csv",
	                     "kml": "https://opendata.arcgis.com/datasets/5d90eeb4db7d49ab99f0565ff612eb1c_0.kml",
	                     "shp": "https://opendata.arcgis.com/datasets/5d90eeb4db7d49ab99f0565ff612eb1c_0.zip",
	                     "gdb": "https://www.arcgis.com/sharing/rest/content/items/90e0d0e513e64056a988cbb67054196b/data"},
	    "metaUrl": "https://services.arcgis.com/ZpeBVw5o1kjit7LT/arcgis/rest/services/PlacesOfWorship/FeatureServer?f=pjson",
	    "attributeUrl": "https://services.arcgis.com/ZpeBVw5o1kjit7LT/arcgis/rest/services/PlacesOfWorship/FeatureServer/layers?f=pjon",
	    "popupFields": ["NAME","ADDRESS"]},
	"schools":{
	    "endpoint": "https://services.arcgis.com/ZpeBVw5o1kjit7LT/arcgis/rest/services/Schools/FeatureServer/0/",
	    "downloadUrls": {"csv": "https://opendata.arcgis.com/datasets/3901b3ef7f7343be8ebfe793efae8f21_0.csv",
	                     "kml": "https://opendata.arcgis.com/datasets/3901b3ef7f7343be8ebfe793efae8f21_0.kml",
	                     "shp": "https://opendata.arcgis.com/datasets/3901b3ef7f7343be8ebfe793efae8f21_0.zip",
	                     "gdb": "https://www.arcgis.com/sharing/rest/content/items/397f1b3e570a4ec2b393e9bb528dc3de/data"},
	    "metaUrl": "https://services.arcgis.com/ZpeBVw5o1kjit7LT/arcgis/rest/services/Schools/FeatureServer?f=pjson",
	    "attributesUrl": "https://services.arcgis.com/ZpeBVw5o1kjit7LT/arcgis/rest/services/Schools/FeatureServer/layers?f=pjson",
	    "popupFields": ["NAME","TYPE","ADDRESS","URL"]}
	}

