# EMA Hourly Continuation — KSM/USDT P21_200

**Symbol:** KSM/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.6006 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8650 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -3.0430 |
| sortino_ratio | -0.7833 |
| max_drawdown | 0.6391 |
| cagr | -0.3204 |
| net_avg_win | 58.7285 |
| net_avg_loss | -84.0363 |
| avg_hold_time_bars | 42.1134 |
| exposure | 0.6585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
