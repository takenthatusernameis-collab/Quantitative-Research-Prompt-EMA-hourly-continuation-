# EMA Hourly Continuation — FLOW/USDT P12_144

**Symbol:** FLOW/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.5966 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 0.9048 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -3.7369 |
| sortino_ratio | -1.1749 |
| max_drawdown | 0.7730 |
| cagr | -0.4356 |
| net_avg_win | 48.1810 |
| net_avg_loss | -69.7289 |
| avg_hold_time_bars | 29.4772 |
| exposure | 0.6766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
