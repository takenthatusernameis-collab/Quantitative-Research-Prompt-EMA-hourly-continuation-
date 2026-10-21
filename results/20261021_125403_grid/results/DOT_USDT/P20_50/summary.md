# EMA Hourly Continuation — DOT/USDT P20_50

**Symbol:** DOT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.8788 |
| net_win_rate | 0.5481 |
| gross_profit_factor | 1.2090 |
| gross_win_rate | 0.5481 |
| sharpe_ratio | -0.8670 |
| sortino_ratio | -0.2751 |
| max_drawdown | 0.3660 |
| cagr | -0.1210 |
| net_avg_win | 76.5581 |
| net_avg_loss | -105.6730 |
| avg_hold_time_bars | 7.6799 |
| exposure | 0.1669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
