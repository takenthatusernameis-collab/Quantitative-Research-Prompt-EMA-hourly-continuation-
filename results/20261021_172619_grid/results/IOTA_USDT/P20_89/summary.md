# EMA Hourly Continuation — IOTA/USDT P20_89

**Symbol:** IOTA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.6976 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8803 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -2.8198 |
| sortino_ratio | -0.8848 |
| max_drawdown | 0.6647 |
| cagr | -0.3347 |
| net_avg_win | 66.2596 |
| net_avg_loss | -79.9330 |
| avg_hold_time_bars | 16.8811 |
| exposure | 0.3745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
