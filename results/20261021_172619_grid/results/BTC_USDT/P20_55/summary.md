# EMA Hourly Continuation — BTC/USDT P20_55

**Symbol:** BTC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.5366 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.9377 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -4.5923 |
| sortino_ratio | -1.4252 |
| max_drawdown | 0.8485 |
| cagr | -0.4838 |
| net_avg_win | 39.6205 |
| net_avg_loss | -65.3969 |
| avg_hold_time_bars | 9.7102 |
| exposure | 0.2051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
