# EMA Hourly Continuation — IOTA/USDT P8_55

**Symbol:** IOTA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.8318 |
| net_win_rate | 0.5142 |
| gross_profit_factor | 1.0563 |
| gross_win_rate | 0.5142 |
| sharpe_ratio | -1.5142 |
| sortino_ratio | -0.5638 |
| max_drawdown | 0.5261 |
| cagr | -0.2307 |
| net_avg_win | 69.1561 |
| net_avg_loss | -87.9833 |
| avg_hold_time_bars | 16.7303 |
| exposure | 0.5103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
