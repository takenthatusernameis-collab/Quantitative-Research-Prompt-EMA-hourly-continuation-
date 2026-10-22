# EMA Hourly Continuation — CATI/USDT P89_200

**Symbol:** CATI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 237 |
| net_profit_factor | 0.6319 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.7830 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -2.3565 |
| sortino_ratio | -0.5642 |
| max_drawdown | 0.4176 |
| cagr | -0.2287 |
| net_avg_win | 68.2887 |
| net_avg_loss | -85.9583 |
| avg_hold_time_bars | 13.2405 |
| exposure | 0.1720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
