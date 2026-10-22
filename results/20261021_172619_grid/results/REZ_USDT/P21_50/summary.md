# EMA Hourly Continuation — REZ/USDT P21_50

**Symbol:** REZ/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.7922 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 1.0033 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -1.9365 |
| sortino_ratio | -0.6425 |
| max_drawdown | 0.5916 |
| cagr | -0.2555 |
| net_avg_win | 75.3986 |
| net_avg_loss | -93.3923 |
| avg_hold_time_bars | 7.5690 |
| exposure | 0.1847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
