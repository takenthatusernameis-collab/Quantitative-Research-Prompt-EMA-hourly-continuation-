# EMA Hourly Continuation — BSV/USDT P8_100

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 793 |
| net_profit_factor | 0.5070 |
| net_win_rate | 0.4174 |
| gross_profit_factor | 0.8202 |
| gross_win_rate | 0.4313 |
| sharpe_ratio | -6.7041 |
| sortino_ratio | -2.6188 |
| max_drawdown | 0.9639 |
| cagr | -0.7296 |
| net_avg_win | 29.9097 |
| net_avg_loss | -42.2633 |
| avg_hold_time_bars | 17.9899 |
| exposure | 0.6485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
