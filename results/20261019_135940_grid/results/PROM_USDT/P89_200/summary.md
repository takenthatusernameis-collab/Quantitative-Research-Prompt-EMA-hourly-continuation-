# EMA Hourly Continuation — PROM/USDT P89_200

**Symbol:** PROM/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.3409 |
| net_win_rate | 0.3698 |
| gross_profit_factor | 0.6501 |
| gross_win_rate | 0.4091 |
| sharpe_ratio | -6.7294 |
| sortino_ratio | -2.0813 |
| max_drawdown | 0.9274 |
| cagr | -0.6475 |
| net_avg_win | 26.7889 |
| net_avg_loss | -46.1190 |
| avg_hold_time_bars | 10.0000 |
| exposure | 0.2200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
