# EMA Hourly Continuation — CATI/USDT P12_21

**Symbol:** CATI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1295 |
| net_profit_factor | 0.2957 |
| net_win_rate | 0.3467 |
| gross_profit_factor | 0.5663 |
| gross_win_rate | 0.3761 |
| sharpe_ratio | -15.9938 |
| sortino_ratio | -9.0440 |
| max_drawdown | 1.0000 |
| cagr | -0.9915 |
| net_avg_win | 9.3503 |
| net_avg_loss | -16.7823 |
| avg_hold_time_bars | 2.5645 |
| exposure | 0.1820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
