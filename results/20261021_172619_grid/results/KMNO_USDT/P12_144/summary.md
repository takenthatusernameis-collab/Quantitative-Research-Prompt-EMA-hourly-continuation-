# EMA Hourly Continuation — KMNO/USDT P12_144

**Symbol:** KMNO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.8088 |
| net_win_rate | 0.4910 |
| gross_profit_factor | 0.9641 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -1.2262 |
| sortino_ratio | -0.3220 |
| max_drawdown | 0.3495 |
| cagr | -0.1393 |
| net_avg_win | 79.9239 |
| net_avg_loss | -95.3268 |
| avg_hold_time_bars | 43.1707 |
| exposure | 0.6657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
