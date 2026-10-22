# EMA Hourly Continuation — FLUX/USDT P89_200

**Symbol:** FLUX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.9706 |
| net_win_rate | 0.5524 |
| gross_profit_factor | 1.2219 |
| gross_win_rate | 0.5524 |
| sharpe_ratio | -0.1050 |
| sortino_ratio | -0.0258 |
| max_drawdown | 0.1832 |
| cagr | -0.0168 |
| net_avg_win | 86.9310 |
| net_avg_loss | -110.5588 |
| avg_hold_time_bars | 15.1958 |
| exposure | 0.1975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
