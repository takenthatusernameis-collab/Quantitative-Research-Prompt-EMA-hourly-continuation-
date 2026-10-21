# EMA Hourly Continuation — GRAM/USDT P8_50

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.7320 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 1.0030 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -2.6073 |
| sortino_ratio | -0.9459 |
| max_drawdown | 0.7008 |
| cagr | -0.3524 |
| net_avg_win | 56.8649 |
| net_avg_loss | -76.7242 |
| avg_hold_time_bars | 13.9875 |
| exposure | 0.4082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
