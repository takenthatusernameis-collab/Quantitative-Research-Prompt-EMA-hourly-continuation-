# EMA Hourly Continuation — XEC/USDT P26_50

**Symbol:** XEC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.7097 |
| net_win_rate | 0.5009 |
| gross_profit_factor | 1.0791 |
| gross_win_rate | 0.5009 |
| sharpe_ratio | -3.1454 |
| sortino_ratio | -1.0677 |
| max_drawdown | 0.7593 |
| cagr | -0.3862 |
| net_avg_win | 61.8388 |
| net_avg_loss | -87.4411 |
| avg_hold_time_bars | 6.4401 |
| exposure | 0.1629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
