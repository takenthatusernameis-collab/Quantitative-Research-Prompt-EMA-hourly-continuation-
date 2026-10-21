# EMA Hourly Continuation — CVX/USDT P21_89

**Symbol:** CVX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.7877 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 0.9734 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -1.6429 |
| sortino_ratio | -0.5339 |
| max_drawdown | 0.4787 |
| cagr | -0.2189 |
| net_avg_win | 66.9875 |
| net_avg_loss | -83.7383 |
| avg_hold_time_bars | 13.8391 |
| exposure | 0.3246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
