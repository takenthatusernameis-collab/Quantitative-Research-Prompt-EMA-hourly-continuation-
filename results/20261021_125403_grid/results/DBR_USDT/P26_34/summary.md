# EMA Hourly Continuation — DBR/USDT P26_34

**Symbol:** DBR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 200 |
| net_profit_factor | 0.5278 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9410 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -3.0500 |
| sortino_ratio | -0.6895 |
| max_drawdown | 0.4906 |
| cagr | -0.2740 |
| net_avg_win | 55.7713 |
| net_avg_loss | -95.6128 |
| avg_hold_time_bars | 8.3450 |
| exposure | 0.0949 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
