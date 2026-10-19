# EMA Hourly Continuation — XDC/USDT P89_200

**Symbol:** XDC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.3036 |
| net_win_rate | 0.4056 |
| gross_profit_factor | 0.7078 |
| gross_win_rate | 0.4418 |
| sharpe_ratio | -7.0521 |
| sortino_ratio | -2.2134 |
| max_drawdown | 0.9502 |
| cagr | -0.6951 |
| net_avg_win | 20.4905 |
| net_avg_loss | -46.0558 |
| avg_hold_time_bars | 7.5361 |
| exposure | 0.1706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
