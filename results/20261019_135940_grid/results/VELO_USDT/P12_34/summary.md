# EMA Hourly Continuation — VELO/USDT P12_34

**Symbol:** VELO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1363 |
| net_profit_factor | 0.5493 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.8646 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -7.5207 |
| sortino_ratio | -3.9061 |
| max_drawdown | 0.9921 |
| cagr | -0.8515 |
| net_avg_win | 19.2488 |
| net_avg_loss | -29.9389 |
| avg_hold_time_bars | 3.8254 |
| exposure | 0.2370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
