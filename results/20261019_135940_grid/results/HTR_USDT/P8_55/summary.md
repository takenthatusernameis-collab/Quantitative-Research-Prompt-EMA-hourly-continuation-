# EMA Hourly Continuation — HTR/USDT P8_55

**Symbol:** HTR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1122 |
| net_profit_factor | 0.5197 |
| net_win_rate | 0.4020 |
| gross_profit_factor | 0.7801 |
| gross_win_rate | 0.4118 |
| sharpe_ratio | -8.3040 |
| sortino_ratio | -3.8906 |
| max_drawdown | 0.9918 |
| cagr | -0.8509 |
| net_avg_win | 23.7897 |
| net_avg_loss | -30.7678 |
| avg_hold_time_bars | 8.6078 |
| exposure | 0.4390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
