When we test code that involves timeouts or intervals, instead of having our tests wait it out or timeout, we can speed up our tests by using "fake" timers that mock calls to setTimeout and setInterval.

See the vi.useFakeTimers API section for a more in depth detailed API description.

## Example ​