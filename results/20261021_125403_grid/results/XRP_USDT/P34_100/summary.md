# EMA Hourly Continuation — XRP/USDT P34_100

**Symbol:** XRP/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.6428 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9274 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -2.6032 |
| sortino_ratio | -0.7254 |
| max_drawdown | 0.6013 |
| cagr | -0.2816 |
| net_avg_win | 55.4745 |
| net_avg_loss | -80.5794 |
| avg_hold_time_bars | 14.5620 |
| exposure | 0.2509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
