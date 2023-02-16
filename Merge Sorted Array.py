def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    n3 = nums1 + nums2
    nums1 = n3
    nums1.sort()
    print(n3)
    print(nums1)

merge([1,2,3,0,0,0],3,[2,5,6],3)
