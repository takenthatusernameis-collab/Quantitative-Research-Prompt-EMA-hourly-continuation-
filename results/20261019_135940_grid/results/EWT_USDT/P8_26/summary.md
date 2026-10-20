# EMA Hourly Continuation — EWT/USDT P8_26

**Symbol:** EWT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1384 |
| net_profit_factor | 0.3274 |
| net_win_rate | 0.3678 |
| gross_profit_factor | 0.6134 |
| gross_win_rate | 0.3887 |
| sharpe_ratio | -13.2054 |
| sortino_ratio | -6.9405 |
| max_drawdown | 0.9999 |
| cagr | -0.9728 |
| net_avg_win | 9.5618 |
| net_avg_loss | -16.9895 |
| avg_hold_time_bars | 4.0224 |
| exposure | 0.2530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
