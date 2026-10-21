# EMA Hourly Continuation — SUN/USDT P21_50

**Symbol:** SUN/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.4459 |
| net_win_rate | 0.4139 |
| gross_profit_factor | 0.8169 |
| gross_win_rate | 0.4333 |
| sharpe_ratio | -6.6551 |
| sortino_ratio | -2.1757 |
| max_drawdown | 0.9275 |
| cagr | -0.6466 |
| net_avg_win | 34.8719 |
| net_avg_loss | -55.2389 |
| avg_hold_time_bars | 9.8956 |
| exposure | 0.2315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
