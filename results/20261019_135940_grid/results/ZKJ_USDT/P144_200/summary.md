# EMA Hourly Continuation — ZKJ/USDT P144_200

**Symbol:** ZKJ/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.2412 |
| net_win_rate | 0.3602 |
| gross_profit_factor | 0.7841 |
| gross_win_rate | 0.4165 |
| sharpe_ratio | -8.3004 |
| sortino_ratio | -2.6128 |
| max_drawdown | 0.9722 |
| cagr | -0.7533 |
| net_avg_win | 17.2310 |
| net_avg_loss | -40.2098 |
| avg_hold_time_bars | 5.6519 |
| exposure | 0.1277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
