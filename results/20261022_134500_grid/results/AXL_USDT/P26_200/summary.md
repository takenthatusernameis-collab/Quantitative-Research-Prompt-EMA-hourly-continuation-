# EMA Hourly Continuation — AXL/USDT P26_200

**Symbol:** AXL/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.7225 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9660 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -2.3306 |
| sortino_ratio | -0.7044 |
| max_drawdown | 0.5670 |
| cagr | -0.2815 |
| net_avg_win | 66.9575 |
| net_avg_loss | -85.3050 |
| avg_hold_time_bars | 26.8606 |
| exposure | 0.5579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
