# EMA Hourly Continuation — IOTA/USDT P26_34

**Symbol:** IOTA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1104 |
| net_profit_factor | 0.2210 |
| net_win_rate | 0.3632 |
| gross_profit_factor | 0.6823 |
| gross_win_rate | 0.4130 |
| sharpe_ratio | -13.1866 |
| sortino_ratio | -6.3560 |
| max_drawdown | 0.9997 |
| cagr | -0.9630 |
| net_avg_win | 7.0735 |
| net_avg_loss | -18.2560 |
| avg_hold_time_bars | 2.1350 |
| exposure | 0.1071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
