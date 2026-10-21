# EMA Hourly Continuation — LQTY/USDT P12_21

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.6357 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9189 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -3.1906 |
| sortino_ratio | -1.0201 |
| max_drawdown | 0.7034 |
| cagr | -0.3724 |
| net_avg_win | 50.4765 |
| net_avg_loss | -72.7064 |
| avg_hold_time_bars | 4.9480 |
| exposure | 0.1120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
