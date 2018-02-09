<?php
	header('Content-Type: application/json');
	echo json_encode([
	    "resolutionList"=>[
	        [
	            "w"=>1920,
	            "h"=>1080
	        ],
	        [
	            "w"=>1440,
	            "h"=>900
	        ],
	        [
	            "w"=>1366,
	            "h"=>1080
	        ],
	        [
	            "w"=>1920,
	            "h"=>1080
	        ],
	        [
	            "w"=>1920,
	            "h"=>1080
	        ],
	    ],
	    "siteList"=>[
	        [
	            "link"=>"https://habrahabr.ru/post/348634/#comment_10659356",
	            'resolutionList'=> [
                    [
                        'w'=> 900,
                        'h'=> 765,
                    ],
                    [
                        'w'=> 1488,
                        'h'=> 228,
                    ],
                ],
	        ],
	        [
                'link'=> 'http://selenium-python.readthedocs.io/',
                'resolutionList'=> [],
            ],
            [
                'link'=> 'http://moringa.labgrape.com',
                'resolutionList'=> [],
            ],
	    ]
	]);