# EMA Hourly Continuation — WEMIX/USDT P34_55

**Symbol:** WEMIX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.5180 |
| net_win_rate | 0.4086 |
| gross_profit_factor | 0.7064 |
| gross_win_rate | 0.4086 |
| sharpe_ratio | -3.4357 |
| sortino_ratio | -0.7828 |
| max_drawdown | 0.5985 |
| cagr | -0.3047 |
| net_avg_win | 61.2551 |
| net_avg_loss | -81.6891 |
| avg_hold_time_bars | 7.8949 |
| exposure | 0.0922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
