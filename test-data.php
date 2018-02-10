<?php
	header('Content-Type: application/json');
	echo json_encode([
	    "resolutionList"=>[
	        [
	            "w"=>1920,
	            "h"=>1080
	        ],

	    ],
	    "siteList"=>[
	        [
                'link'=> 'http://selenium-python.readthedocs.io/',
                'resolutionList'=> [],
            ],
	    ]
	]);