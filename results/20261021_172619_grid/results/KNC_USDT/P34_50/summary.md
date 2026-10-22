# EMA Hourly Continuation — KNC/USDT P34_50

**Symbol:** KNC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.5780 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9777 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -3.5736 |
| sortino_ratio | -1.0302 |
| max_drawdown | 0.7003 |
| cagr | -0.3773 |
| net_avg_win | 48.6131 |
| net_avg_loss | -80.8054 |
| avg_hold_time_bars | 6.0675 |
| exposure | 0.1103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
