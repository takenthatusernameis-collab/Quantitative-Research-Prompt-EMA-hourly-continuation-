# EMA Hourly Continuation — NEAR/USDT P89_200

**Symbol:** NEAR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6374 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9664 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -2.6646 |
| sortino_ratio | -0.7348 |
| max_drawdown | 0.5964 |
| cagr | -0.2942 |
| net_avg_win | 55.4235 |
| net_avg_loss | -81.2382 |
| avg_hold_time_bars | 11.5274 |
| exposure | 0.2007 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
