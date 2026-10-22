# EMA Hourly Continuation — MAGIC/USDT P8_144

**Symbol:** MAGIC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.8198 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9852 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -1.3134 |
| sortino_ratio | -0.3706 |
| max_drawdown | 0.4512 |
| cagr | -0.1582 |
| net_avg_win | 82.7821 |
| net_avg_loss | -98.9263 |
| avg_hold_time_bars | 41.7282 |
| exposure | 0.7397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
