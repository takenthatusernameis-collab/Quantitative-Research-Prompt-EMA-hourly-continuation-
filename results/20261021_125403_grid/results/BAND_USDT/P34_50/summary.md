# EMA Hourly Continuation — BAND/USDT P34_50

**Symbol:** BAND/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.6519 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0033 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -2.8610 |
| sortino_ratio | -0.8676 |
| max_drawdown | 0.6573 |
| cagr | -0.3264 |
| net_avg_win | 52.9873 |
| net_avg_loss | -81.2795 |
| avg_hold_time_bars | 5.2466 |
| exposure | 0.1059 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
