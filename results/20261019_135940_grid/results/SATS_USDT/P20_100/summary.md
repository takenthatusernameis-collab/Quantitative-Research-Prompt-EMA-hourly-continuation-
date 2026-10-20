# EMA Hourly Continuation — SATS/USDT P20_100

**Symbol:** SATS/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.6855 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.9571 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -3.2486 |
| sortino_ratio | -1.1340 |
| max_drawdown | 0.7753 |
| cagr | -0.4152 |
| net_avg_win | 55.3514 |
| net_avg_loss | -72.5518 |
| avg_hold_time_bars | 14.9546 |
| exposure | 0.4175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
