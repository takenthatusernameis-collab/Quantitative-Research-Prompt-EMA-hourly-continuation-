# EMA Hourly Continuation — CATI/USDT P8_34

**Symbol:** CATI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1183 |
| net_profit_factor | 0.4934 |
| net_win_rate | 0.4057 |
| gross_profit_factor | 0.7718 |
| gross_win_rate | 0.4243 |
| sharpe_ratio | -10.6275 |
| sortino_ratio | -5.6525 |
| max_drawdown | 0.9971 |
| cagr | -0.9393 |
| net_avg_win | 20.2329 |
| net_avg_loss | -27.9980 |
| avg_hold_time_bars | 5.3660 |
| exposure | 0.3480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
