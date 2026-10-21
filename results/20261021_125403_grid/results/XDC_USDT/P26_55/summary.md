# EMA Hourly Continuation — XDC/USDT P26_55

**Symbol:** XDC/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.5348 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8644 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -3.5319 |
| sortino_ratio | -0.9975 |
| max_drawdown | 0.6932 |
| cagr | -0.3684 |
| net_avg_win | 43.2477 |
| net_avg_loss | -71.4418 |
| avg_hold_time_bars | 7.6108 |
| exposure | 0.1342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
