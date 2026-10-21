# EMA Hourly Continuation — PYTH/USDT P100_144

**Symbol:** PYTH/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 218 |
| net_profit_factor | 0.8334 |
| net_win_rate | 0.5229 |
| gross_profit_factor | 1.0819 |
| gross_win_rate | 0.5229 |
| sharpe_ratio | -0.7900 |
| sortino_ratio | -0.1683 |
| max_drawdown | 0.2450 |
| cagr | -0.0752 |
| net_avg_win | 78.2235 |
| net_avg_loss | -102.8852 |
| avg_hold_time_bars | 6.9174 |
| exposure | 0.0685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
