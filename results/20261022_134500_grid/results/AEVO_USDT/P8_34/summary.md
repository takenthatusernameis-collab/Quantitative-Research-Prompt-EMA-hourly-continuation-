# EMA Hourly Continuation — AEVO/USDT P8_34

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1339 |
| net_profit_factor | 0.5410 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.8774 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -6.9914 |
| sortino_ratio | -3.5910 |
| max_drawdown | 0.9881 |
| cagr | -0.8229 |
| net_avg_win | 18.8874 |
| net_avg_loss | -29.7478 |
| avg_hold_time_bars | 6.1113 |
| exposure | 0.3703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
