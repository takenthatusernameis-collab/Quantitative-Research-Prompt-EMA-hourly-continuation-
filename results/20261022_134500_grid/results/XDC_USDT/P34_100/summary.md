# EMA Hourly Continuation — XDC/USDT P34_100

**Symbol:** XDC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 744 |
| net_profit_factor | 0.2923 |
| net_win_rate | 0.4220 |
| gross_profit_factor | 0.7428 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -8.2095 |
| sortino_ratio | -3.1134 |
| max_drawdown | 0.9855 |
| cagr | -0.8125 |
| net_avg_win | 12.9574 |
| net_avg_loss | -32.3703 |
| avg_hold_time_bars | 7.7285 |
| exposure | 0.2614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
