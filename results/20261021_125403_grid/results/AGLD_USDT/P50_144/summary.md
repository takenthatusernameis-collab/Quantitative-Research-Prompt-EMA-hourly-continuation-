# EMA Hourly Continuation — AGLD/USDT P50_144

**Symbol:** AGLD/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.6997 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 0.8890 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -2.4675 |
| sortino_ratio | -0.7094 |
| max_drawdown | 0.5782 |
| cagr | -0.2780 |
| net_avg_win | 68.7000 |
| net_avg_loss | -84.7966 |
| avg_hold_time_bars | 15.3463 |
| exposure | 0.2847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
