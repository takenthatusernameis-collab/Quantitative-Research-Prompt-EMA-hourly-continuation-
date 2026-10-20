# EMA Hourly Continuation — XYO/USDT P21_200

**Symbol:** XYO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.5513 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.8463 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -4.2426 |
| sortino_ratio | -1.2938 |
| max_drawdown | 0.8079 |
| cagr | -0.4674 |
| net_avg_win | 45.6898 |
| net_avg_loss | -66.9306 |
| avg_hold_time_bars | 27.9916 |
| exposure | 0.6067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
