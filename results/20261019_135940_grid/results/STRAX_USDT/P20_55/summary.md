# EMA Hourly Continuation — STRAX/USDT P20_55

**Symbol:** STRAX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 954 |
| net_profit_factor | 0.5018 |
| net_win_rate | 0.4172 |
| gross_profit_factor | 0.8288 |
| gross_win_rate | 0.4382 |
| sharpe_ratio | -8.2520 |
| sortino_ratio | -3.5878 |
| max_drawdown | 0.9886 |
| cagr | -0.8334 |
| net_avg_win | 25.0141 |
| net_avg_loss | -35.6864 |
| avg_hold_time_bars | 7.1069 |
| exposure | 0.3100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
