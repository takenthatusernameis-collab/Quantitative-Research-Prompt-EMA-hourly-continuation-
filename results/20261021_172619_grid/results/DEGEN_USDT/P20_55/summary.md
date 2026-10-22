# EMA Hourly Continuation — DEGEN/USDT P20_55

**Symbol:** DEGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.8386 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0261 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -1.4027 |
| sortino_ratio | -0.4605 |
| max_drawdown | 0.4468 |
| cagr | -0.1928 |
| net_avg_win | 81.7672 |
| net_avg_loss | -99.0083 |
| avg_hold_time_bars | 8.7634 |
| exposure | 0.2091 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
