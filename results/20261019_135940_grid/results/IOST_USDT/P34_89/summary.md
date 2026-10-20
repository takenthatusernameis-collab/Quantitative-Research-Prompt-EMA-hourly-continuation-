# EMA Hourly Continuation — IOST/USDT P34_89

**Symbol:** IOST/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.5661 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 1.0290 |
| gross_win_rate | 0.5127 |
| sharpe_ratio | -4.4433 |
| sortino_ratio | -1.6151 |
| max_drawdown | 0.8708 |
| cagr | -0.5451 |
| net_avg_win | 33.9633 |
| net_avg_loss | -58.7528 |
| avg_hold_time_bars | 8.4096 |
| exposure | 0.2557 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
