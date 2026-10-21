# EMA Hourly Continuation — THETA/USDT P34_50

**Symbol:** THETA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.6781 |
| net_win_rate | 0.4957 |
| gross_profit_factor | 0.9564 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -1.7268 |
| sortino_ratio | -0.3796 |
| max_drawdown | 0.3761 |
| cagr | -0.1580 |
| net_avg_win | 63.7002 |
| net_avg_loss | -92.3492 |
| avg_hold_time_bars | 5.5085 |
| exposure | 0.0586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
