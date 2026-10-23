# EMA Hourly Continuation — KAVA/USDT P26_200

**Symbol:** KAVA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.6159 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.9432 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -3.6783 |
| sortino_ratio | -1.0803 |
| max_drawdown | 0.7410 |
| cagr | -0.4060 |
| net_avg_win | 58.5036 |
| net_avg_loss | -80.4958 |
| avg_hold_time_bars | 27.9381 |
| exposure | 0.5537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
