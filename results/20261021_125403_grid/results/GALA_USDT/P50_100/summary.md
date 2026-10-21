# EMA Hourly Continuation — GALA/USDT P50_100

**Symbol:** GALA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.7002 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.8946 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -2.1594 |
| sortino_ratio | -0.5989 |
| max_drawdown | 0.5150 |
| cagr | -0.2401 |
| net_avg_win | 65.0012 |
| net_avg_loss | -83.5058 |
| avg_hold_time_bars | 10.1772 |
| exposure | 0.1749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
