import android
import urllib
droid=android.Android()

layout="""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:id="@+id/background"
	android:orientation="vertical" android:layout_width="match_parent"
	android:layout_height="match_parent" android:background="#ff000000">
	<LinearLayout android:layout_width="match_parent"
		android:layout_height="wrap_content" android:id="@+id/linearLayout1">
			<Button android:id="@+id/button_daily" android:layout_width="wrap_content"
				android:layout_height="wrap_content" android:text="Daily"></Button>
			<Button android:id="@+id/button_weekly" android:layout_width="wrap_content"
				android:layout_height="wrap_content" android:text="Weekly"></Button>
			<Button android:id="@+id/button_monthly" android:layout_width="wrap_content"
				android:layout_height="wrap_content" android:text="Monthly"></Button>
			<Button android:id="@+id/button_monthly_avg" android:layout_width="wrap_content"
				android:layout_height="wrap_content" android:text="Monthly Average"></Button>
	</LinearLayout>
	<ImageView android:id="@+id/imageview"
		android:src="@drawable/brush"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	<Button android:id="@+id/button_quit" android:layout_width="wrap_content"
		android:layout_height="wrap_content" android:text="Quit"></Button>
</LinearLayout>
"""
def eventloop():
	while True:
		event=droid.eventWait().result
		print event
		if event["name"]=="click":
			id=event["data"]["id"]
			if id=="button_daily":
				change_weather("daily")
			elif id=="button_weekly":
				change_weather("weekly")
			elif id=="button_monthly":
				change_weather("monthly")
			elif id=="button_monthly_avg":
				change_weather("monthlyAVG")
			elif id=="button_quit":
				return
		elif event["name"]=="screen":
			if event["data"]=="destroy":
				return

def change_weather(timeframe):
	urllib.urlretrieve("http://sheeva.wippiespace.com/%s.png" % timeframe, "/sdcard/download/%s.png" % timeframe)
	droid.fullSetProperty("imageview","src","file:///sdcard/download/%s.png" % timeframe)
	
def main():
	print droid.fullShow(layout)
	eventloop()
	droid.fullDismiss()

if __name__ == "__main__":
	main()
