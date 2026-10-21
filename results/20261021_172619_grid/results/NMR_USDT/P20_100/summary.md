# EMA Hourly Continuation — NMR/USDT P20_100

**Symbol:** NMR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.7721 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9885 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -2.0058 |
| sortino_ratio | -0.6509 |
| max_drawdown | 0.5680 |
| cagr | -0.2585 |
| net_avg_win | 70.1592 |
| net_avg_loss | -88.7814 |
| avg_hold_time_bars | 18.1744 |
| exposure | 0.4263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
