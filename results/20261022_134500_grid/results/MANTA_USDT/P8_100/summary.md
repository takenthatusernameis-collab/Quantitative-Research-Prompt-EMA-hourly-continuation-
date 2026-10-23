# EMA Hourly Continuation — MANTA/USDT P8_100

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.6460 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.9306 |
| gross_win_rate | 0.4662 |
| sharpe_ratio | -4.0591 |
| sortino_ratio | -1.4522 |
| max_drawdown | 0.8306 |
| cagr | -0.5026 |
| net_avg_win | 50.4577 |
| net_avg_loss | -66.5407 |
| avg_hold_time_bars | 23.4477 |
| exposure | 0.6928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
