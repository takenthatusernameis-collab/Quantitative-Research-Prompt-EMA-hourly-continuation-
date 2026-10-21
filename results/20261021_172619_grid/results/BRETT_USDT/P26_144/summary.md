# EMA Hourly Continuation — BRETT/USDT P26_144

**Symbol:** BRETT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.7594 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.8664 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -1.4766 |
| sortino_ratio | -0.3787 |
| max_drawdown | 0.3518 |
| cagr | -0.1608 |
| net_avg_win | 74.5871 |
| net_avg_loss | -86.2358 |
| avg_hold_time_bars | 35.1981 |
| exposure | 0.5216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
