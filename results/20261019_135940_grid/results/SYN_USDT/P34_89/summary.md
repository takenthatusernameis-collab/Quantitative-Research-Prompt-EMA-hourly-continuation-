# EMA Hourly Continuation — SYN/USDT P34_89

**Symbol:** SYN/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.6196 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 0.9648 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -4.0280 |
| sortino_ratio | -1.4533 |
| max_drawdown | 0.8356 |
| cagr | -0.5096 |
| net_avg_win | 42.6611 |
| net_avg_loss | -62.7380 |
| avg_hold_time_bars | 9.2699 |
| exposure | 0.2810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
