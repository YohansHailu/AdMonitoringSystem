
#img1 = cv2.imread("walia bira ad.jpeg")
#img2 = cv2.imread("walia bira ad_copy.jpeg")
#img3 = cv2.imread("walia bira_2.jpg")
#print(are_matching_sift_knn(img1, img3))

#walia_beer_frame = cv2.imread("walia bira_2.jpg")
#walia_ad_file_name = "./WALIA BEER TVC (Directors' Cut) [DPJBDupSiwA].webm"
#random_walia_frame = get_random_frame(walia_ad_file_name)
#cv2.imwrite("random walie frame.jpg", random_walia_frame)
#print(are_matching_sift_knn(random_walia_frame, walia_beer_frame))

#walia_beer_frame = cv2.imread("walia bira_2.jpg")
#walia_ad_file_name = "./WALIA BEER TVC (Directors' Cut) [DPJBDupSiwA].webm"
#res = matching_frame_in_video(walia_ad_file_name, walia_beer_frame)


frame_a = cv2.imread("./data_file/sample_rand_frame.jpg")
walia_ad_file_name  = "./data_file/WALIA BEER TVC (Directors' Cut) [DPJBDupSiwA].webm"
res = matching_frame_in_video(walia_ad_file_name, frame_a)
print(res)


#video_file_name = "./WALIA BEER TVC (Directors' Cut) [DPJBDupSiwA].webm"
#random_frame = get_random_frame(video_file_name, 0.2)
#random_frame2 = get_random_frame(video_file_name, 0.2)
#cv2.imwrite("rand_img.jpg",random_frame)
#cv2.imwrite("rand_imge2.jpg",random_frame2)
#
#_, index_a =  matching_frame_in_video(video_file_name, random_frame2)
#_, index_b =  matching_frame_in_video(video_file_name, random_frame)
#print(index_a)
#print(index_b)
#print(get_time_two_frames(video_file_name,random_frame, random_frame2), "s")



#img1 = cv2.imread("walia bira ad.jpeg")
#img2 = cv2.imread("walia bira ad_copy.jpeg")
#img3 = cv2.imread("walia bira_2.jpg")
#print(are_matching_template_matching(img1, img2))

