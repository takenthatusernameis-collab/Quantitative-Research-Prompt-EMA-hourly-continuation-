# EMA Hourly Continuation — CSPR/USDT P8_34

**Symbol:** CSPR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.6175 |
| net_win_rate | 0.4323 |
| gross_profit_factor | 0.7860 |
| gross_win_rate | 0.4323 |
| sharpe_ratio | -4.0693 |
| sortino_ratio | -1.4615 |
| max_drawdown | 0.8161 |
| cagr | -0.4905 |
| net_avg_win | 47.3828 |
| net_avg_loss | -58.4469 |
| avg_hold_time_bars | 8.1384 |
| exposure | 0.2379 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
