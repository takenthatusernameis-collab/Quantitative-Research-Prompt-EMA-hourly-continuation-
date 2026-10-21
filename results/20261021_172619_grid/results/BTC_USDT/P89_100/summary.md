# EMA Hourly Continuation — BTC/USDT P89_100

**Symbol:** BTC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 100 |
| net_profit_factor | 0.4062 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.9341 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -2.3134 |
| sortino_ratio | -0.3163 |
| max_drawdown | 0.3381 |
| cagr | -0.1323 |
| net_avg_win | 48.4723 |
| net_avg_loss | -105.8323 |
| avg_hold_time_bars | 4.8800 |
| exposure | 0.0195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
