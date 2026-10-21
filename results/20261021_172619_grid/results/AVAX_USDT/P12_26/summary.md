# EMA Hourly Continuation — AVAX/USDT P12_26

**Symbol:** AVAX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.6254 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8665 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -3.3381 |
| sortino_ratio | -0.9625 |
| max_drawdown | 0.6824 |
| cagr | -0.3572 |
| net_avg_win | 60.8358 |
| net_avg_loss | -79.9015 |
| avg_hold_time_bars | 5.3971 |
| exposure | 0.1001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
