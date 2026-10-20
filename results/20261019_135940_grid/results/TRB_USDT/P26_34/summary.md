# EMA Hourly Continuation — TRB/USDT P26_34

**Symbol:** TRB/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1179 |
| net_profit_factor | 0.2924 |
| net_win_rate | 0.3486 |
| gross_profit_factor | 0.7116 |
| gross_win_rate | 0.4080 |
| sharpe_ratio | -14.1667 |
| sortino_ratio | -7.0352 |
| max_drawdown | 0.9999 |
| cagr | -0.9752 |
| net_avg_win | 10.0528 |
| net_avg_loss | -18.3995 |
| avg_hold_time_bars | 2.0237 |
| exposure | 0.1080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
