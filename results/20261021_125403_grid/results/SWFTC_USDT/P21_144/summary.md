# EMA Hourly Continuation — SWFTC/USDT P21_144

**Symbol:** SWFTC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7454 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9073 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -1.9052 |
| sortino_ratio | -0.5252 |
| max_drawdown | 0.4608 |
| cagr | -0.2152 |
| net_avg_win | 74.9681 |
| net_avg_loss | -90.4171 |
| avg_hold_time_bars | 26.8112 |
| exposure | 0.4582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
