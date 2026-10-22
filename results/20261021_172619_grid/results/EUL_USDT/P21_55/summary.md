# EMA Hourly Continuation — EUL/USDT P21_55

**Symbol:** EUL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.6115 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.7953 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -2.8900 |
| sortino_ratio | -0.9032 |
| max_drawdown | 0.6627 |
| cagr | -0.3394 |
| net_avg_win | 45.8708 |
| net_avg_loss | -64.0489 |
| avg_hold_time_bars | 9.7137 |
| exposure | 0.2128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
