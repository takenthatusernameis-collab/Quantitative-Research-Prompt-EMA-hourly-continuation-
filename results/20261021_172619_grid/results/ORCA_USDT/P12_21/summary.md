# EMA Hourly Continuation — ORCA/USDT P12_21

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.7193 |
| net_win_rate | 0.5183 |
| gross_profit_factor | 1.0946 |
| gross_win_rate | 0.5224 |
| sharpe_ratio | -2.3884 |
| sortino_ratio | -0.7617 |
| max_drawdown | 0.6224 |
| cagr | -0.2954 |
| net_avg_win | 58.7715 |
| net_avg_loss | -87.9173 |
| avg_hold_time_bars | 5.1504 |
| exposure | 0.1152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
