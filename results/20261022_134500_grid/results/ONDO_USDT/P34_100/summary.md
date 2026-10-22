# EMA Hourly Continuation — ONDO/USDT P34_100

**Symbol:** ONDO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.5759 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.8599 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -5.0233 |
| sortino_ratio | -1.8133 |
| max_drawdown | 0.8930 |
| cagr | -0.5857 |
| net_avg_win | 40.7218 |
| net_avg_loss | -56.9121 |
| avg_hold_time_bars | 8.3514 |
| exposure | 0.2528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
