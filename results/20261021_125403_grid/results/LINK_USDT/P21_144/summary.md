# EMA Hourly Continuation — LINK/USDT P21_144

**Symbol:** LINK/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.8380 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0429 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -1.0121 |
| sortino_ratio | -0.2718 |
| max_drawdown | 0.3384 |
| cagr | -0.1186 |
| net_avg_win | 78.5261 |
| net_avg_loss | -98.0922 |
| avg_hold_time_bars | 31.8914 |
| exposure | 0.5074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
