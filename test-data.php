<?php
	header("Content-Type: application/json");
	echo json_encode([
	    "resolutionList"=>[
	        [
	            "w"=>1024,
	            "h"=>768
	        ]
	    ],
	    "siteList"=>[
	        [
                "link"=> "https://reactjs.org/docs/forms.html",
                "resolutionList"=> [
                ],
            ],
	        [
                "link"=> "http://timotei-promo.labgrape.com/",
                "resolutionList"=> [
                ],
            ],
	    ]
	]);