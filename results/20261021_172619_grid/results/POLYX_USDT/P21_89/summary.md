# EMA Hourly Continuation — POLYX/USDT P21_89

**Symbol:** POLYX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.7799 |
| net_win_rate | 0.5009 |
| gross_profit_factor | 1.0112 |
| gross_win_rate | 0.5009 |
| sharpe_ratio | -1.9696 |
| sortino_ratio | -0.6566 |
| max_drawdown | 0.5870 |
| cagr | -0.2606 |
| net_avg_win | 69.2575 |
| net_avg_loss | -89.1281 |
| avg_hold_time_bars | 14.4162 |
| exposure | 0.3558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
