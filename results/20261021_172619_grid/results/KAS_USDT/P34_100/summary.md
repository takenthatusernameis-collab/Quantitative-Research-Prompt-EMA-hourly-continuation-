# EMA Hourly Continuation — KAS/USDT P34_100

**Symbol:** KAS/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7479 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -1.7355 |
| sortino_ratio | -0.4886 |
| max_drawdown | 0.4399 |
| cagr | -0.2011 |
| net_avg_win | 66.9443 |
| net_avg_loss | -87.2221 |
| avg_hold_time_bars | 11.8062 |
| exposure | 0.2077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
