# EMA Hourly Continuation — BIGTIME/USDT P55_144

**Symbol:** BIGTIME/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.8446 |
| net_win_rate | 0.5121 |
| gross_profit_factor | 1.0617 |
| gross_win_rate | 0.5121 |
| sharpe_ratio | -1.0636 |
| sortino_ratio | -0.2935 |
| max_drawdown | 0.3410 |
| cagr | -0.1275 |
| net_avg_win | 83.2880 |
| net_avg_loss | -103.5141 |
| avg_hold_time_bars | 15.0162 |
| exposure | 0.2521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
