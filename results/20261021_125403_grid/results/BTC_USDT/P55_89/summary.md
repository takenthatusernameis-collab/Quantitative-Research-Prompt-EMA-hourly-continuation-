# EMA Hourly Continuation — BTC/USDT P55_89

**Symbol:** BTC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.4951 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9996 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -3.5267 |
| sortino_ratio | -0.8472 |
| max_drawdown | 0.6695 |
| cagr | -0.3198 |
| net_avg_win | 43.3243 |
| net_avg_loss | -82.5812 |
| avg_hold_time_bars | 7.1672 |
| exposure | 0.0892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
