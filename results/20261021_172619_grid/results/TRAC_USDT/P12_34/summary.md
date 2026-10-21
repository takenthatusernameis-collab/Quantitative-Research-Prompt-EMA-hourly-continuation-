# EMA Hourly Continuation — TRAC/USDT P12_34

**Symbol:** TRAC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.7227 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9539 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -2.4988 |
| sortino_ratio | -0.8206 |
| max_drawdown | 0.6299 |
| cagr | -0.3135 |
| net_avg_win | 62.4623 |
| net_avg_loss | -80.7287 |
| avg_hold_time_bars | 9.3902 |
| exposure | 0.2254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
