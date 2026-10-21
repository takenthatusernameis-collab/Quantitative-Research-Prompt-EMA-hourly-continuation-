# EMA Hourly Continuation — CRO/USDT P20_50

**Symbol:** CRO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.5724 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.8563 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -3.8396 |
| sortino_ratio | -1.2243 |
| max_drawdown | 0.7640 |
| cagr | -0.4299 |
| net_avg_win | 43.8248 |
| net_avg_loss | -66.4845 |
| avg_hold_time_bars | 8.3340 |
| exposure | 0.1883 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
