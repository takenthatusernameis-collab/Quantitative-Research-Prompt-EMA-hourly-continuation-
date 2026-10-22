# EMA Hourly Continuation — SNX/USDT P50_89

**Symbol:** SNX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.6135 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 1.1028 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -4.8946 |
| sortino_ratio | -1.7918 |
| max_drawdown | 0.8976 |
| cagr | -0.5904 |
| net_avg_win | 42.0266 |
| net_avg_loss | -65.9619 |
| avg_hold_time_bars | 4.7881 |
| exposure | 0.1493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
