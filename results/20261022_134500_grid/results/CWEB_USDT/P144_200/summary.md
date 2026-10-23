# EMA Hourly Continuation — CWEB/USDT P144_200

**Symbol:** CWEB/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.4792 |
| net_win_rate | 0.4221 |
| gross_profit_factor | 0.8832 |
| gross_win_rate | 0.4325 |
| sharpe_ratio | -4.7168 |
| sortino_ratio | -1.1355 |
| max_drawdown | 0.7722 |
| cagr | -0.4383 |
| net_avg_win | 57.7060 |
| net_avg_loss | -87.9705 |
| avg_hold_time_bars | 6.8962 |
| exposure | 0.0906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
