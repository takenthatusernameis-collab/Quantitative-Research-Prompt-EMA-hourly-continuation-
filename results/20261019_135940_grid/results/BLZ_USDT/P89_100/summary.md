# EMA Hourly Continuation — BLZ/USDT P89_100

**Symbol:** BLZ/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.3729 |
| net_win_rate | 0.3737 |
| gross_profit_factor | 0.9455 |
| gross_win_rate | 0.4104 |
| sharpe_ratio | -9.5638 |
| sortino_ratio | -3.5045 |
| max_drawdown | 0.9901 |
| cagr | -0.8388 |
| net_avg_win | 24.1263 |
| net_avg_loss | -38.5980 |
| avg_hold_time_bars | 3.7779 |
| exposure | 0.1116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
