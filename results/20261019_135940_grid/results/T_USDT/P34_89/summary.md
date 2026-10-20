# EMA Hourly Continuation — T/USDT P34_89

**Symbol:** T/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.5448 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.8921 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -5.1592 |
| sortino_ratio | -1.7899 |
| max_drawdown | 0.8925 |
| cagr | -0.5811 |
| net_avg_win | 38.3953 |
| net_avg_loss | -58.6242 |
| avg_hold_time_bars | 9.4590 |
| exposure | 0.2611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
