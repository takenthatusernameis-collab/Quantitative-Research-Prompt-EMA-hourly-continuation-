# EMA Hourly Continuation — SUN/USDT P26_50

**Symbol:** SUN/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.3851 |
| net_win_rate | 0.4032 |
| gross_profit_factor | 0.7652 |
| gross_win_rate | 0.4234 |
| sharpe_ratio | -6.7089 |
| sortino_ratio | -2.0442 |
| max_drawdown | 0.9161 |
| cagr | -0.6256 |
| net_avg_win | 32.0552 |
| net_avg_loss | -56.2215 |
| avg_hold_time_bars | 8.5338 |
| exposure | 0.1715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
