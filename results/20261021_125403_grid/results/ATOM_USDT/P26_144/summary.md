# EMA Hourly Continuation — ATOM/USDT P26_144

**Symbol:** ATOM/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.8793 |
| net_win_rate | 0.5288 |
| gross_profit_factor | 1.1037 |
| gross_win_rate | 0.5288 |
| sharpe_ratio | -0.6712 |
| sortino_ratio | -0.1849 |
| max_drawdown | 0.3117 |
| cagr | -0.0847 |
| net_avg_win | 75.2630 |
| net_avg_loss | -96.0424 |
| avg_hold_time_bars | 28.3425 |
| exposure | 0.4702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
