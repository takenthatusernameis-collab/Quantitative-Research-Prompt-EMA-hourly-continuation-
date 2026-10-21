# EMA Hourly Continuation — XNO/USDT P26_100

**Symbol:** XNO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.6146 |
| net_win_rate | 0.4266 |
| gross_profit_factor | 0.7658 |
| gross_win_rate | 0.4266 |
| sharpe_ratio | -3.6464 |
| sortino_ratio | -1.1497 |
| max_drawdown | 0.7414 |
| cagr | -0.4109 |
| net_avg_win | 55.3107 |
| net_avg_loss | -66.9417 |
| avg_hold_time_bars | 14.1107 |
| exposure | 0.3188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
