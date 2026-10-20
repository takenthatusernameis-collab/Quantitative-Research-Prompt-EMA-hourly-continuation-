# EMA Hourly Continuation — HNT/USDT P8_55

**Symbol:** HNT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1067 |
| net_profit_factor | 0.4950 |
| net_win_rate | 0.4377 |
| gross_profit_factor | 0.7552 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -6.7169 |
| sortino_ratio | -3.0796 |
| max_drawdown | 0.9778 |
| cagr | -0.7749 |
| net_avg_win | 20.4923 |
| net_avg_loss | -32.2226 |
| avg_hold_time_bars | 10.1649 |
| exposure | 0.4930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
