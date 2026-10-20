# EMA Hourly Continuation — CELR/USDT P100_144

**Symbol:** CELR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.3759 |
| net_win_rate | 0.4114 |
| gross_profit_factor | 0.6868 |
| gross_win_rate | 0.4193 |
| sharpe_ratio | -6.1880 |
| sortino_ratio | -1.9793 |
| max_drawdown | 0.9120 |
| cagr | -0.6171 |
| net_avg_win | 26.2571 |
| net_avg_loss | -48.8301 |
| avg_hold_time_bars | 4.3307 |
| exposure | 0.0996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
