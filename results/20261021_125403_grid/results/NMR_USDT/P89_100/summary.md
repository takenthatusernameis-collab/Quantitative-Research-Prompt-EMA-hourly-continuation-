# EMA Hourly Continuation — NMR/USDT P89_100

**Symbol:** NMR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 157 |
| net_profit_factor | 0.5529 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.8564 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -2.2513 |
| sortino_ratio | -0.4043 |
| max_drawdown | 0.3975 |
| cagr | -0.1694 |
| net_avg_win | 64.9089 |
| net_avg_loss | -96.9190 |
| avg_hold_time_bars | 6.3376 |
| exposure | 0.0452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
