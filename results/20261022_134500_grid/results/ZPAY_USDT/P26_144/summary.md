# EMA Hourly Continuation — ZPAY/USDT P26_144

**Symbol:** ZPAY/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.5307 |
| net_win_rate | 0.3814 |
| gross_profit_factor | 0.6567 |
| gross_win_rate | 0.3840 |
| sharpe_ratio | -4.0670 |
| sortino_ratio | -1.1153 |
| max_drawdown | 0.7351 |
| cagr | -0.4073 |
| net_avg_win | 55.9769 |
| net_avg_loss | -65.0486 |
| avg_hold_time_bars | 34.6933 |
| exposure | 0.6091 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
