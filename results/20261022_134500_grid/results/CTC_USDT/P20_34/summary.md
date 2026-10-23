# EMA Hourly Continuation — CTC/USDT P20_34

**Symbol:** CTC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1140 |
| net_profit_factor | 0.2846 |
| net_win_rate | 0.3991 |
| gross_profit_factor | 0.7796 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -11.4680 |
| sortino_ratio | -5.5386 |
| max_drawdown | 0.9992 |
| cagr | -0.9397 |
| net_avg_win | 8.7357 |
| net_avg_loss | -20.3884 |
| avg_hold_time_bars | 3.2702 |
| exposure | 0.1695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
