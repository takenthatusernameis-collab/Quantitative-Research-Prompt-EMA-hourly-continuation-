# EMA Hourly Continuation — SAND/USDT P55_144

**Symbol:** SAND/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.6454 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.8291 |
| gross_win_rate | 0.4519 |
| sharpe_ratio | -2.4394 |
| sortino_ratio | -0.6122 |
| max_drawdown | 0.5112 |
| cagr | -0.2452 |
| net_avg_win | 65.3846 |
| net_avg_loss | -83.5409 |
| avg_hold_time_bars | 19.2981 |
| exposure | 0.2737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
