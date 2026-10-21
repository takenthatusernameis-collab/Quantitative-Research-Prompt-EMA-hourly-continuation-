# EMA Hourly Continuation — VELO/USDT P21_144

**Symbol:** VELO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.9456 |
| net_win_rate | 0.5257 |
| gross_profit_factor | 1.0954 |
| gross_win_rate | 0.5257 |
| sharpe_ratio | -0.3043 |
| sortino_ratio | -0.0907 |
| max_drawdown | 0.2932 |
| cagr | -0.0471 |
| net_avg_win | 88.1910 |
| net_avg_loss | -103.3744 |
| avg_hold_time_bars | 26.3294 |
| exposure | 0.5122 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
