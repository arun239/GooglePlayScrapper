var GoogleAppAdmin = angular.module('GoogleAppAdmin', []);
GoogleAppAdmin
		.controller(
				'displayListOfAppsController',
				[
						'$scope',
						'$rootScope',
						'$http',
						'$window',
						'$location',
						function($scope, $rootScope, $http, $window, $location) {
							
							$scope.getAppList = function() {
								$http({
								cache : false,
								method : 'GET',
								url : 'https://nq6y9xdf4d.execute-api.us-east-1.amazonaws.com/prod/packages',
								headers : {
									'Accept' : 'application/json'
									
								}
							}).then(function successCallback(response) {
								$scope.appsList = response.data;
								$scope.loading = false;

							}, function errorCallback(response) {
								$scope.loading = false;
								$scope.appsList = response.data;
								alert("Error in fetching app list");
							});
							}
							
							$scope.contextPath = window.location.pathname
									.substring(0, window.location.pathname
											.indexOf("/", 2));
							$scope.loading = true;	
							$scope.getAppList();
										
							
							

							$scope.showAppInfo = function(selectedPackage) {
								$scope.displayAppInfo = false;
								$scope.loading = true;
								$scope.individualAppResp = null;
								//$scope.selectedAppName = selectedApp["app_name"];
								$scope.selectedPackage = selectedPackage;
								console.log("selected package: ", selectedPackage);
								$http(
										{
											cache : false,
											method : 'GET',
											url : 'https://nq6y9xdf4d.execute-api.us-east-1.amazonaws.com/prod/package-info' + '?package_name=' +
													+ selectedPackage,
											headers : {
												'Accept' : 'application/json'	
											}

										})
										.then(
												function successCallback(
														response) {
													$scope.displayAppInfo = true;
													$scope.individualAppResp = response.data;
													$scope.loading = false;
													console.log("received app data : " + $scope.individualAppResp);
												},
												function errorCallback(response) {
													$scope.individualAppResp = response.data;
													console.log("received app data : ", $scope.individualAppResp);
													$scope.loading = false;
												});
							};

							$scope.track = function() {
								if (angular.isUndefined($scope.packageName) || $scope.packageName === null) {
									alert("Please enter package name to be tracked");
									return false;
								}
								var jsonData = {
									'package_name' : $scope.packageName,
									'app_name' : $scope.appName
									};
									$http({
										cache : false,
										method : 'POST',
										url : 'https://nq6y9xdf4d.execute-api.us-east-1.amazonaws.com/prod/packages',
										data : jsonData
											})
											.then(
													function successCallback(
															response) {
														alert("Package is added to tracking list");
														$scope.getAppList();
														
															},
															function errorCallback(
																	response) {
														alert(Error);
															});
							}
							
							
								
														
						} ]);