# EMA Hourly Continuation — POLYX/USDT P55_144

**Symbol:** POLYX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.7721 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0112 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.6601 |
| sortino_ratio | -0.4586 |
| max_drawdown | 0.4361 |
| cagr | -0.1902 |
| net_avg_win | 74.9243 |
| net_avg_loss | -97.0364 |
| avg_hold_time_bars | 14.7312 |
| exposure | 0.2491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
