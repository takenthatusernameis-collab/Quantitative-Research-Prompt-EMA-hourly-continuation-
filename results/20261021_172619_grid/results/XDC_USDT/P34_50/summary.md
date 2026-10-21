# EMA Hourly Continuation — XDC/USDT P34_50

**Symbol:** XDC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 204 |
| net_profit_factor | 0.5662 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9500 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -2.4869 |
| sortino_ratio | -0.5111 |
| max_drawdown | 0.4794 |
| cagr | -0.2089 |
| net_avg_win | 59.2445 |
| net_avg_loss | -96.7424 |
| avg_hold_time_bars | 7.5980 |
| exposure | 0.0705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
