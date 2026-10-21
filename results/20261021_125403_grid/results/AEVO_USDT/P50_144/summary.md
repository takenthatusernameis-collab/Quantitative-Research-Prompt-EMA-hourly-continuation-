# EMA Hourly Continuation — AEVO/USDT P50_144

**Symbol:** AEVO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.8044 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9988 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.3587 |
| sortino_ratio | -0.3783 |
| max_drawdown | 0.3712 |
| cagr | -0.1611 |
| net_avg_win | 77.4530 |
| net_avg_loss | -96.2901 |
| avg_hold_time_bars | 18.0684 |
| exposure | 0.3107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
