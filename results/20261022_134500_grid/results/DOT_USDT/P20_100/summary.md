# EMA Hourly Continuation — DOT/USDT P20_100

**Symbol:** DOT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.6793 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0844 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -3.1954 |
| sortino_ratio | -1.1169 |
| max_drawdown | 0.7578 |
| cagr | -0.4149 |
| net_avg_win | 50.2268 |
| net_avg_loss | -75.8824 |
| avg_hold_time_bars | 15.6542 |
| exposure | 0.4383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
