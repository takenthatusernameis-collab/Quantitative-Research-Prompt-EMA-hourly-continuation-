# EMA Hourly Continuation — ATOM/USDT P26_200

**Symbol:** ATOM/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6391 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 0.9224 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -2.5013 |
| sortino_ratio | -0.6785 |
| max_drawdown | 0.5857 |
| cagr | -0.2789 |
| net_avg_win | 54.4910 |
| net_avg_loss | -80.4055 |
| avg_hold_time_bars | 33.2800 |
| exposure | 0.5673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
