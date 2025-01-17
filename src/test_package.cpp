#include <Poco/Net/Net.h>
#include <Poco/Net/ServerSocket.h>

int main(int, char**)
{
	Poco::Net::initializeNetwork();
	// Will cause linker error due to undefined reference to TransmitFile while using MinGW
	Poco::Net::ServerSocket socket(9876);
	
	Poco::Net::uninitializeNetwork();
	return 0;
}

