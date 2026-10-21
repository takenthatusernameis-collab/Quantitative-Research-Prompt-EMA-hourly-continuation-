# EMA Hourly Continuation — XTZ/USDT P21_26

**Symbol:** XTZ/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.6239 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0199 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.3032 |
| sortino_ratio | -0.5094 |
| max_drawdown | 0.4609 |
| cagr | -0.2064 |
| net_avg_win | 62.4372 |
| net_avg_loss | -100.0803 |
| avg_hold_time_bars | 4.3504 |
| exposure | 0.0463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
