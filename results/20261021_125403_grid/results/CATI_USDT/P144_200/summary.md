# EMA Hourly Continuation — CATI/USDT P144_200

**Symbol:** CATI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 187 |
| net_profit_factor | 0.5044 |
| net_win_rate | 0.3957 |
| gross_profit_factor | 0.6472 |
| gross_win_rate | 0.3957 |
| sharpe_ratio | -3.1465 |
| sortino_ratio | -0.6677 |
| max_drawdown | 0.4881 |
| cagr | -0.2653 |
| net_avg_win | 65.1625 |
| net_avg_loss | -84.5964 |
| avg_hold_time_bars | 7.5508 |
| exposure | 0.0774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
