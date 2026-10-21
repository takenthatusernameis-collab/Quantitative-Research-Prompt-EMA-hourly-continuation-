# EMA Hourly Continuation — AURORA/USDT P50_144

**Symbol:** AURORA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.6664 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.8933 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -2.2976 |
| sortino_ratio | -0.5759 |
| max_drawdown | 0.4907 |
| cagr | -0.2325 |
| net_avg_win | 66.8818 |
| net_avg_loss | -88.7406 |
| avg_hold_time_bars | 18.9968 |
| exposure | 0.2668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
