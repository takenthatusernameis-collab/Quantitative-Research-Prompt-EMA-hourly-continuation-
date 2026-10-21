# EMA Hourly Continuation — XTZ/USDT P20_21

**Symbol:** XTZ/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.6474 |
| net_win_rate | 0.5109 |
| gross_profit_factor | 1.0513 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -1.8302 |
| sortino_ratio | -0.3592 |
| max_drawdown | 0.3626 |
| cagr | -0.1504 |
| net_avg_win | 65.6013 |
| net_avg_loss | -105.8289 |
| avg_hold_time_bars | 4.0870 |
| exposure | 0.0342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
