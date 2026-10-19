# EMA Hourly Continuation — ZRO/USDT P34_50

**Symbol:** ZRO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 884 |
| net_profit_factor | 0.5006 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.9229 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -7.1826 |
| sortino_ratio | -3.1144 |
| max_drawdown | 0.9734 |
| cagr | -0.7880 |
| net_avg_win | 23.9669 |
| net_avg_loss | -40.8510 |
| avg_hold_time_bars | 2.6075 |
| exposure | 0.1128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
