# EMA Hourly Continuation — AR/USDT P26_89

**Symbol:** AR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.5691 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.8604 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -4.3481 |
| sortino_ratio | -1.5847 |
| max_drawdown | 0.8591 |
| cagr | -0.5395 |
| net_avg_win | 35.6057 |
| net_avg_loss | -54.5105 |
| avg_hold_time_bars | 10.2665 |
| exposure | 0.3187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
