import hashlib as blake2b
import platform
import random as rand
import tracemalloc
import numpy



#print(resource.getrusage(resource.RUSAGE_SELF))
#resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

def genRandByteStr(n):
    byte_str = rand.randbytes(n)
    return byte_str

#function that calculates the digest of the hashlib object's hash function
#digest method is isolated to measure execution time
#@profile
def runHashFunction(hash_obj):
    dig = hash_obj.digest()
    return dig

#@profile
def main():
    avail_alg = blake2b.algorithms_available
    #sha_set = {'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'sha512_224', 'sha512_256', 'sha3_224', 'sha3_256','sha3_384', 'sha3_512'}
    #sha_avail = avail_alg.intersection(sha_set)

    blake_func = {'blake2b', 'blake2s'}
    blake_avail = avail_alg.intersection(blake_func)

    rand.seed()


    input_size = [1, 1024, 1048576]

    # system info for comparison
    print("System info:")
    arc = platform.architecture()
    mach = platform.machine()
    plat = platform.platform(aliased=1, terse=1)
    proc = platform.processor()
    print("Architecture: {}\tMachine: {}\tPlatform: {}\tProcessor {}".format(arc, mach, plat, proc))


    for x in blake_avail:

        currMemUsage = numpy.zeros((100), dtype=int)
        peakMemUsage = numpy.zeros((100), dtype=int)

        blake_func = blake2b.new(x)
        print("====================================================================================================")
        print("Using hash function " + x)

        for i in input_size:

            tracemalloc.start()

            for j in range(100):
                # start tracing memory allocation


                # Generation of plaintext used as input into hash function
                ByteLength = i
                print("Using input size: {}".format(i))
                ptext = genRandByteStr(ByteLength)
                blake_func.update(ptext)

                dig = blake_func.digest()
                print("\tDigest: {}".format(dig))

                #store mem usage
                currMemUsage[j], peakMemUsage[j] = tracemalloc.get_traced_memory()

                # stopping the library
                #currMemUsage.append(tracemalloc.get_traced_memory())
                #peakMemUsage.append(tracemalloc.get_traced_memory())

            #print(peakMemUsage)
            tracemalloc.stop()
            print("Current Memory Usage")
            print(currMemUsage)
            print("Average Current Memory")
            print(numpy.mean(currMemUsage))
            print("Peak Memory Usage")
            print(peakMemUsage)
            print("Average Peak Memory")
            print(numpy.mean(peakMemUsage))

            # displaying the memory
            #print(tracemalloc.get_traced_memory())

        print("====================================================================================================")
        print()

        #print(currMemUsage)
        #print(f"{currMemUsage = }, {peakMemUsage = }")
        #print(resource.getrusage(resource.RUSAGE_SELF))

if __name__ == '__main__':
    main()