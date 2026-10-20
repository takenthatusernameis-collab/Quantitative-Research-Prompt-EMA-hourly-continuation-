# EMA Hourly Continuation — BOME/USDT P8_144

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.6158 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.8785 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -2.8692 |
| sortino_ratio | -0.8756 |
| max_drawdown | 0.6940 |
| cagr | -0.3479 |
| net_avg_win | 45.8855 |
| net_avg_loss | -68.0031 |
| avg_hold_time_bars | 34.3465 |
| exposure | 0.7525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
