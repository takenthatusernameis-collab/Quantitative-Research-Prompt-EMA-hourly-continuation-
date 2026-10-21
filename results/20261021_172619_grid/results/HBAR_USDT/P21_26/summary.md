# EMA Hourly Continuation — HBAR/USDT P21_26

**Symbol:** HBAR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 135 |
| net_profit_factor | 0.7050 |
| net_win_rate | 0.5111 |
| gross_profit_factor | 1.0384 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -1.2541 |
| sortino_ratio | -0.2099 |
| max_drawdown | 0.2470 |
| cagr | -0.0914 |
| net_avg_win | 74.0751 |
| net_avg_loss | -109.8516 |
| avg_hold_time_bars | 4.8370 |
| exposure | 0.0297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
