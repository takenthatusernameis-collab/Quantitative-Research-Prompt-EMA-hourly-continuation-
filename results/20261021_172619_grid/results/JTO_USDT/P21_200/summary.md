# EMA Hourly Continuation — JTO/USDT P21_200

**Symbol:** JTO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.8127 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.9319 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -1.1882 |
| sortino_ratio | -0.2980 |
| max_drawdown | 0.3987 |
| cagr | -0.1295 |
| net_avg_win | 85.0613 |
| net_avg_loss | -97.5121 |
| avg_hold_time_bars | 43.3023 |
| exposure | 0.6121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
