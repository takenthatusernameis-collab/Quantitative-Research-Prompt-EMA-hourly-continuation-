# EMA Hourly Continuation — ASTR/USDT P12_26

**Symbol:** ASTR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.6795 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 1.0467 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -3.6883 |
| sortino_ratio | -1.3217 |
| max_drawdown | 0.7890 |
| cagr | -0.4577 |
| net_avg_win | 53.7810 |
| net_avg_loss | -76.9158 |
| avg_hold_time_bars | 5.8076 |
| exposure | 0.1653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
