# EMA Hourly Continuation — COMP/USDT P55_100

**Symbol:** COMP/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.4892 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9792 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -5.1081 |
| sortino_ratio | -1.8478 |
| max_drawdown | 0.9042 |
| cagr | -0.5978 |
| net_avg_win | 26.4715 |
| net_avg_loss | -51.7289 |
| avg_hold_time_bars | 5.1970 |
| exposure | 0.1571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
