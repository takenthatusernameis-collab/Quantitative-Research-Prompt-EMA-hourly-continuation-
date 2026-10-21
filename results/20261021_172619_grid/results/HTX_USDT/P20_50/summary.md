# EMA Hourly Continuation — HTX/USDT P20_50

**Symbol:** HTX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.3886 |
| net_win_rate | 0.3868 |
| gross_profit_factor | 0.6843 |
| gross_win_rate | 0.3962 |
| sharpe_ratio | -7.2452 |
| sortino_ratio | -2.4143 |
| max_drawdown | 0.9432 |
| cagr | -0.6792 |
| net_avg_win | 29.2480 |
| net_avg_loss | -47.4691 |
| avg_hold_time_bars | 9.5415 |
| exposure | 0.2288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
