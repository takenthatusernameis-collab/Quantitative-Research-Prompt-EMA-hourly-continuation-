# EMA Hourly Continuation — AXL/USDT P34_200

**Symbol:** AXL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7901 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.9372 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -1.4730 |
| sortino_ratio | -0.4012 |
| max_drawdown | 0.3900 |
| cagr | -0.1699 |
| net_avg_win | 79.7097 |
| net_avg_loss | -93.9850 |
| avg_hold_time_bars | 29.8801 |
| exposure | 0.4962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
