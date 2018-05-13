#include <stdio.h>
#include <motors/driver.h>

int main()
{
	setCodingWheelLeftOrientation(1);
	setCodingWheelRightOrientation(0);
	printf("%d", getCodingWheelLeftOrientation());	
	printf("%d", getCodingWheelRightOrientation());
	writeMotorsFlash();
	return 0;
}

