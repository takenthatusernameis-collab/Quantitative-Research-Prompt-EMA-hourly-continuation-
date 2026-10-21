# EMA Hourly Continuation — ANKR/USDT P12_50

**Symbol:** ANKR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.7123 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.9545 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -3.4040 |
| sortino_ratio | -1.2323 |
| max_drawdown | 0.7689 |
| cagr | -0.4332 |
| net_avg_win | 62.0694 |
| net_avg_loss | -77.4307 |
| avg_hold_time_bars | 13.6335 |
| exposure | 0.3991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
