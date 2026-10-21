# EMA Hourly Continuation — SUPER/USDT P21_144

**Symbol:** SUPER/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.9307 |
| net_win_rate | 0.5332 |
| gross_profit_factor | 1.1297 |
| gross_win_rate | 0.5332 |
| sharpe_ratio | -0.3838 |
| sortino_ratio | -0.1096 |
| max_drawdown | 0.2545 |
| cagr | -0.0542 |
| net_avg_win | 83.9394 |
| net_avg_loss | -103.0016 |
| avg_hold_time_bars | 28.8010 |
| exposure | 0.5132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
