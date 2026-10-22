# EMA Hourly Continuation — DASH/USDT P12_21

**Symbol:** DASH/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1488 |
| net_profit_factor | 0.1462 |
| net_win_rate | 0.3985 |
| gross_profit_factor | 0.6067 |
| gross_win_rate | 0.4409 |
| sharpe_ratio | -13.9164 |
| sortino_ratio | -7.6709 |
| max_drawdown | 1.0000 |
| cagr | -0.9823 |
| net_avg_win | 2.8873 |
| net_avg_loss | -13.0858 |
| avg_hold_time_bars | 2.1754 |
| exposure | 0.1471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
