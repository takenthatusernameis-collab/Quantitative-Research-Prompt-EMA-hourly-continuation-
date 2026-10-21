# EMA Hourly Continuation — ANKR/USDT P12_21

**Symbol:** ANKR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.6158 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9590 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -3.6394 |
| sortino_ratio | -1.1616 |
| max_drawdown | 0.7453 |
| cagr | -0.4112 |
| net_avg_win | 49.5316 |
| net_avg_loss | -75.3694 |
| avg_hold_time_bars | 5.4309 |
| exposure | 0.1215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
