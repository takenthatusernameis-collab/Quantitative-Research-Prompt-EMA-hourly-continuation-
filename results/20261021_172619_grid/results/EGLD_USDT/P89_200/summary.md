# EMA Hourly Continuation — EGLD/USDT P89_200

**Symbol:** EGLD/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.7815 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0204 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -1.1297 |
| sortino_ratio | -0.2661 |
| max_drawdown | 0.3208 |
| cagr | -0.1157 |
| net_avg_win | 69.3699 |
| net_avg_loss | -92.1239 |
| avg_hold_time_bars | 16.1673 |
| exposure | 0.1977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
