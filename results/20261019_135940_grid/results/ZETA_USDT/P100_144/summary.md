# EMA Hourly Continuation — ZETA/USDT P100_144

**Symbol:** ZETA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.5450 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.9169 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -5.3032 |
| sortino_ratio | -1.7140 |
| max_drawdown | 0.8850 |
| cagr | -0.5607 |
| net_avg_win | 45.9369 |
| net_avg_loss | -66.0413 |
| avg_hold_time_bars | 4.4701 |
| exposure | 0.1050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
