# EMA Hourly Continuation — MOCA/USDT P20_89

**Symbol:** MOCA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5874 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.9036 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -4.5865 |
| sortino_ratio | -1.7104 |
| max_drawdown | 0.8485 |
| cagr | -0.5575 |
| net_avg_win | 40.8629 |
| net_avg_loss | -59.8004 |
| avg_hold_time_bars | 11.6462 |
| exposure | 0.3713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
