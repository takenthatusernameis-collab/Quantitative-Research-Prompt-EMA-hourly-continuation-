# EMA Hourly Continuation — DEEP/USDT P21_26

**Symbol:** DEEP/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 131 |
| net_profit_factor | 1.2778 |
| net_win_rate | 0.6412 |
| gross_profit_factor | 1.7546 |
| gross_win_rate | 0.6412 |
| sharpe_ratio | 1.0384 |
| sortino_ratio | 0.1989 |
| max_drawdown | 0.0822 |
| cagr | 0.0828 |
| net_avg_win | 95.2486 |
| net_avg_loss | -133.2264 |
| avg_hold_time_bars | 4.3282 |
| exposure | 0.0321 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
