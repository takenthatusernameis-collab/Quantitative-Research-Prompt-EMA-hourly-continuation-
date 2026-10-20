# EMA Hourly Continuation — SWFTC/USDT P21_144

**Symbol:** SWFTC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 572 |
| net_profit_factor | 0.5519 |
| net_win_rate | 0.4266 |
| gross_profit_factor | 0.8241 |
| gross_win_rate | 0.4318 |
| sharpe_ratio | -5.3243 |
| sortino_ratio | -1.7795 |
| max_drawdown | 0.8902 |
| cagr | -0.5836 |
| net_avg_win | 44.8868 |
| net_avg_loss | -60.5014 |
| avg_hold_time_bars | 18.2972 |
| exposure | 0.4757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
