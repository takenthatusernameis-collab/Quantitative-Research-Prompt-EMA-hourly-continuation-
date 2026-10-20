# EMA Hourly Continuation — ANKR/USDT P34_144

**Symbol:** ANKR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.5670 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8802 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -4.3347 |
| sortino_ratio | -1.3479 |
| max_drawdown | 0.8094 |
| cagr | -0.4813 |
| net_avg_win | 48.0697 |
| net_avg_loss | -68.8260 |
| avg_hold_time_bars | 19.3707 |
| exposure | 0.4323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
