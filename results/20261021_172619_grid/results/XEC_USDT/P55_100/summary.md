# EMA Hourly Continuation — XEC/USDT P55_100

**Symbol:** XEC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.5512 |
| net_win_rate | 0.4564 |
| gross_profit_factor | 0.8087 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -3.6169 |
| sortino_ratio | -1.0779 |
| max_drawdown | 0.7162 |
| cagr | -0.3891 |
| net_avg_win | 43.9064 |
| net_avg_loss | -66.8875 |
| avg_hold_time_bars | 6.8555 |
| exposure | 0.1353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
