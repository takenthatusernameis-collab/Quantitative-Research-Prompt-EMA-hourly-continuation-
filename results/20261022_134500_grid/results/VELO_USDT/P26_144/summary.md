# EMA Hourly Continuation — VELO/USDT P26_144

**Symbol:** VELO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.7821 |
| net_win_rate | 0.5076 |
| gross_profit_factor | 1.0260 |
| gross_win_rate | 0.5095 |
| sharpe_ratio | -1.7602 |
| sortino_ratio | -0.5752 |
| max_drawdown | 0.5885 |
| cagr | -0.2367 |
| net_avg_win | 65.9806 |
| net_avg_loss | -86.9571 |
| avg_hold_time_bars | 19.8788 |
| exposure | 0.4771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
