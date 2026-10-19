# EMA Hourly Continuation — CVX/USDT P89_100

**Symbol:** CVX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.2694 |
| net_win_rate | 0.3822 |
| gross_profit_factor | 0.7022 |
| gross_win_rate | 0.4156 |
| sharpe_ratio | -8.7061 |
| sortino_ratio | -2.9354 |
| max_drawdown | 0.9779 |
| cagr | -0.7807 |
| net_avg_win | 17.5058 |
| net_avg_loss | -40.1947 |
| avg_hold_time_bars | 2.8850 |
| exposure | 0.0707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
