# EMA Hourly Continuation — HBAR/USDT P12_50

**Symbol:** HBAR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1124 |
| net_profit_factor | 0.5192 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 0.9148 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -7.1934 |
| sortino_ratio | -3.3623 |
| max_drawdown | 0.9854 |
| cagr | -0.8138 |
| net_avg_win | 20.3056 |
| net_avg_loss | -34.1555 |
| avg_hold_time_bars | 6.2500 |
| exposure | 0.3193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
