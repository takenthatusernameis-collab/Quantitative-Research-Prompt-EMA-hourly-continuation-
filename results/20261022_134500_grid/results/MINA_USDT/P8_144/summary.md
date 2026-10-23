# EMA Hourly Continuation — MINA/USDT P8_144

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.7351 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0152 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -2.0577 |
| sortino_ratio | -0.6350 |
| max_drawdown | 0.5911 |
| cagr | -0.2622 |
| net_avg_win | 61.2228 |
| net_avg_loss | -84.6879 |
| avg_hold_time_bars | 34.7021 |
| exposure | 0.7571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
