# EMA Hourly Continuation — ALGO/USDT P12_55

**Symbol:** ALGO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 991 |
| net_profit_factor | 0.5917 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9747 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -4.7371 |
| sortino_ratio | -2.1052 |
| max_drawdown | 0.9250 |
| cagr | -0.6344 |
| net_avg_win | 27.2151 |
| net_avg_loss | -44.9827 |
| avg_hold_time_bars | 8.4289 |
| exposure | 0.3797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
