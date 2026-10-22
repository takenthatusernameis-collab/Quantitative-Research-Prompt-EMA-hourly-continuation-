# EMA Hourly Continuation — CPOOL/USDT P8_144

**Symbol:** CPOOL/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.8077 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9259 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -1.4750 |
| sortino_ratio | -0.4526 |
| max_drawdown | 0.4439 |
| cagr | -0.1905 |
| net_avg_win | 77.2109 |
| net_avg_loss | -88.8547 |
| avg_hold_time_bars | 31.2151 |
| exposure | 0.6598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
