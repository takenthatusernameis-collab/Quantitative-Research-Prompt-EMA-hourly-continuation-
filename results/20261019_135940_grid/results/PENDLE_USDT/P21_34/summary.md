# EMA Hourly Continuation — PENDLE/USDT P21_34

**Symbol:** PENDLE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1178 |
| net_profit_factor | 0.3892 |
| net_win_rate | 0.4321 |
| gross_profit_factor | 0.7477 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -9.1725 |
| sortino_ratio | -4.4675 |
| max_drawdown | 0.9960 |
| cagr | -0.8875 |
| net_avg_win | 12.4681 |
| net_avg_loss | -24.3720 |
| avg_hold_time_bars | 2.6681 |
| exposure | 0.1429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
