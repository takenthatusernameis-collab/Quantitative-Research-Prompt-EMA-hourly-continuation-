# EMA Hourly Continuation — TRB/USDT P8_144

**Symbol:** TRB/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.7776 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9344 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -1.3090 |
| sortino_ratio | -0.3250 |
| max_drawdown | 0.3446 |
| cagr | -0.1394 |
| net_avg_win | 73.9487 |
| net_avg_loss | -90.8365 |
| avg_hold_time_bars | 56.0557 |
| exposure | 0.7737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
