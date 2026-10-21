# EMA Hourly Continuation — EGLD/USDT P8_144

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.8131 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 0.9955 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -1.2229 |
| sortino_ratio | -0.3479 |
| max_drawdown | 0.4141 |
| cagr | -0.1496 |
| net_avg_win | 73.4460 |
| net_avg_loss | -90.7861 |
| avg_hold_time_bars | 40.3671 |
| exposure | 0.7248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
