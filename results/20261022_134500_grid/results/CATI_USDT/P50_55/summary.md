# EMA Hourly Continuation — CATI/USDT P50_55

**Symbol:** CATI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 756 |
| net_profit_factor | 0.2570 |
| net_win_rate | 0.3254 |
| gross_profit_factor | 0.6302 |
| gross_win_rate | 0.3876 |
| sharpe_ratio | -13.4488 |
| sortino_ratio | -5.9743 |
| max_drawdown | 0.9988 |
| cagr | -0.9595 |
| net_avg_win | 14.0405 |
| net_avg_loss | -26.3557 |
| avg_hold_time_bars | 2.4127 |
| exposure | 0.1000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
