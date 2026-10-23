# EMA Hourly Continuation — SWFTC/USDT P26_144

**Symbol:** SWFTC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.5052 |
| net_win_rate | 0.4193 |
| gross_profit_factor | 0.8044 |
| gross_win_rate | 0.4267 |
| sharpe_ratio | -5.5925 |
| sortino_ratio | -1.8089 |
| max_drawdown | 0.8978 |
| cagr | -0.5948 |
| net_avg_win | 40.4980 |
| net_avg_loss | -57.8842 |
| avg_hold_time_bars | 18.0334 |
| exposure | 0.4418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
