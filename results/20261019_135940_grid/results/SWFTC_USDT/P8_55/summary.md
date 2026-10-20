# EMA Hourly Continuation — SWFTC/USDT P8_55

**Symbol:** SWFTC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1107 |
| net_profit_factor | 0.4903 |
| net_win_rate | 0.4182 |
| gross_profit_factor | 0.7867 |
| gross_win_rate | 0.4300 |
| sharpe_ratio | -8.2758 |
| sortino_ratio | -3.8367 |
| max_drawdown | 0.9921 |
| cagr | -0.8541 |
| net_avg_win | 20.6072 |
| net_avg_loss | -30.2198 |
| avg_hold_time_bars | 8.7073 |
| exposure | 0.4381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
