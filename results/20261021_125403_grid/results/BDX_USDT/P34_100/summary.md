# EMA Hourly Continuation — BDX/USDT P34_100

**Symbol:** BDX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.5340 |
| net_win_rate | 0.4493 |
| gross_profit_factor | 0.8374 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -3.7725 |
| sortino_ratio | -1.0025 |
| max_drawdown | 0.6982 |
| cagr | -0.3709 |
| net_avg_win | 50.8464 |
| net_avg_loss | -77.6751 |
| avg_hold_time_bars | 9.4464 |
| exposure | 0.1481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
