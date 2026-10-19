# EMA Hourly Continuation — CFX/USDT P8_89

**Symbol:** CFX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.6736 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9779 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -3.1344 |
| sortino_ratio | -1.0439 |
| max_drawdown | 0.7360 |
| cagr | -0.3972 |
| net_avg_win | 53.4037 |
| net_avg_loss | -75.7419 |
| avg_hold_time_bars | 26.6538 |
| exposure | 0.6894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
