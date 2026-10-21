# EMA Hourly Continuation — XRP/USDT P21_34

**Symbol:** XRP/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 0.6268 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0106 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.1702 |
| sortino_ratio | -0.4574 |
| max_drawdown | 0.4214 |
| cagr | -0.1895 |
| net_avg_win | 64.3504 |
| net_avg_loss | -102.6599 |
| avg_hold_time_bars | 4.7757 |
| exposure | 0.0465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
