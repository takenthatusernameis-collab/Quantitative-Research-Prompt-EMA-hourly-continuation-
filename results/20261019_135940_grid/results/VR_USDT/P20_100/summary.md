# EMA Hourly Continuation — VR/USDT P20_100

**Symbol:** VR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 785 |
| net_profit_factor | 0.4417 |
| net_win_rate | 0.3312 |
| gross_profit_factor | 0.6528 |
| gross_win_rate | 0.3465 |
| sharpe_ratio | -10.6312 |
| sortino_ratio | -4.1400 |
| max_drawdown | 0.9972 |
| cagr | -0.9034 |
| net_avg_win | 30.3467 |
| net_avg_loss | -34.0227 |
| avg_hold_time_bars | 11.0599 |
| exposure | 0.3946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
