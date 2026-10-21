# EMA Hourly Continuation — MAGIC/USDT P8_89

**Symbol:** MAGIC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.8639 |
| net_win_rate | 0.5145 |
| gross_profit_factor | 1.0692 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -1.1828 |
| sortino_ratio | -0.3862 |
| max_drawdown | 0.4635 |
| cagr | -0.1661 |
| net_avg_win | 87.0630 |
| net_avg_loss | -106.7799 |
| avg_hold_time_bars | 27.6358 |
| exposure | 0.6520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
