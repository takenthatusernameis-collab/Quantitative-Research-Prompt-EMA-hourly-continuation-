# EMA Hourly Continuation — VELO/USDT P21_26

**Symbol:** VELO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 144 |
| net_profit_factor | 0.8195 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0726 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -0.7011 |
| sortino_ratio | -0.1213 |
| max_drawdown | 0.1693 |
| cagr | -0.0544 |
| net_avg_win | 79.3659 |
| net_avg_loss | -105.2681 |
| avg_hold_time_bars | 5.1181 |
| exposure | 0.0335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
