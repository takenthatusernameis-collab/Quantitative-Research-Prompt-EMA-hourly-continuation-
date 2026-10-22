# EMA Hourly Continuation — JASMY/USDT P8_34

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1421 |
| net_profit_factor | 0.4628 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.7693 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -8.3846 |
| sortino_ratio | -4.4331 |
| max_drawdown | 0.9959 |
| cagr | -0.8872 |
| net_avg_win | 13.2990 |
| net_avg_loss | -23.8868 |
| avg_hold_time_bars | 4.9170 |
| exposure | 0.3176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
