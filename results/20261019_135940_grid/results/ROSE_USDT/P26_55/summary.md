# EMA Hourly Continuation — ROSE/USDT P26_55

**Symbol:** ROSE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 976 |
| net_profit_factor | 0.6269 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 1.0405 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -5.9371 |
| sortino_ratio | -2.6148 |
| max_drawdown | 0.9617 |
| cagr | -0.7171 |
| net_avg_win | 34.6858 |
| net_avg_loss | -50.1460 |
| avg_hold_time_bars | 4.3258 |
| exposure | 0.1919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
