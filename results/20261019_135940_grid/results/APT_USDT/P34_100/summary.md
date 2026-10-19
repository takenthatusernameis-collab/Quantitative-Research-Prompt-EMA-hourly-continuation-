# EMA Hourly Continuation — APT/USDT P34_100

**Symbol:** APT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.5913 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9749 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -4.4680 |
| sortino_ratio | -1.6035 |
| max_drawdown | 0.8626 |
| cagr | -0.5430 |
| net_avg_win | 39.8800 |
| net_avg_loss | -61.5296 |
| avg_hold_time_bars | 9.1927 |
| exposure | 0.2733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
