# EMA Hourly Continuation — AEVO/USDT P8_55

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.8069 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 0.9864 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -1.8481 |
| sortino_ratio | -0.6850 |
| max_drawdown | 0.5772 |
| cagr | -0.2723 |
| net_avg_win | 68.7804 |
| net_avg_loss | -83.9917 |
| avg_hold_time_bars | 16.8844 |
| exposure | 0.5157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
