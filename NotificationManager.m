//
//  NotificationManager.m
//  miraclr
//
//  Created by Woodsy Studio on 8/31/17.
//  Copyright © 2017 Woodsy Studio. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <UserNotifications/UserNotifications.h> //imports user notification functionality
@interface NotificationManager : NSObject //defines NotificationManager as an object
//declare our variables
@property UNMutableNotificationContent *content;
@property UNTimeIntervalNotificationTrigger *trigger;
@property UNNotificationRequest *request;
@property UNUserNotificationCenter *center;


//declare our methods
-(void) NotificationApprove;
-(void) NotificationText:(NSString*)text andNumber:(NSString*)index andTime:(int)time;
-(void) NotificationClear:(NSString*)index;

@end


@implementation NotificationManager

//implement our methods

//Implement a method for asking the player whether they will accept notifications from the game
-(void) NotificationApprove {
    UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];
    [center requestAuthorizationWithOptions:(UNAuthorizationOptionAlert + UNAuthorizationOptionSound)
                          completionHandler:^(BOOL granted, NSError * _Nullable error){}];
}
/*
//Create a method that takes notification text, index, and time and set it
-(void) NotificationText:(NSString*)text andNumber:(NSString*)index andTime:(int)time {
    //initialize the content of your notification
    UNMutableNotificationContent* content = [[UNMutableNotificationContent alloc]init];
    //set notification title
    content.title = [NSString localizedUserNotificationStringForKey:@"New miraclr activity" arguments:nil];
    //set notification text to be the argument we passed to this method as "text"
    content.body = [NSString localizedUserNotificationStringForKey:text arguments:nil];
    //set sound to play when notification goes off
    content.sound = [UNNotificationSound defaultSound];
    //set the time the notification will trigger based on the argument we passed as "time", minutes from now
    UNTimeIntervalNotificationTrigger* trigger = [UNTimeIntervalNotificationTrigger triggerWithTimeInterval:time*60 repeats:NO];
    //create a notification request which will pass the content to the notification center
    UNNotificationRequest* request = [UNNotificationRequest requestWithIdentifier:index content:content trigger:trigger];
    //create the notification center and add the request
    UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];
    [center addNotificationRequest:request withCompletionHandler:nil];
    
    
    

}

//implement a method that will clear a notification based on its already given index
-(void) NotificationClear:(NSString*)index {
    //gets the user notification center
    UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];
    //creates an array of identifiers that includes the index we passed to it
    NSArray *array = [NSArray arrayWithObjects:index, nil];
    //removes all pending notifications that have an identifier included in the array
    [center removePendingNotificationRequestsWithIdentifiers:array];
    
}
*/
@end


