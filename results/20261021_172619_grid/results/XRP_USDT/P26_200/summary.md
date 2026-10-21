# EMA Hourly Continuation — XRP/USDT P26_200

**Symbol:** XRP/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7329 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9785 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -1.6240 |
| sortino_ratio | -0.4053 |
| max_drawdown | 0.4031 |
| cagr | -0.1695 |
| net_avg_win | 67.7536 |
| net_avg_loss | -91.2316 |
| avg_hold_time_bars | 40.1020 |
| exposure | 0.5541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
