# EMA Hourly Continuation — FIDA/USDT P12_144

**Symbol:** FIDA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.5949 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8546 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -3.6971 |
| sortino_ratio | -1.1713 |
| max_drawdown | 0.7586 |
| cagr | -0.4271 |
| net_avg_win | 48.3963 |
| net_avg_loss | -66.5355 |
| avg_hold_time_bars | 29.6582 |
| exposure | 0.6831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
