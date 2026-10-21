# EMA Hourly Continuation — BABYDOGE/USDT P12_20

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 11 |
| net_profit_factor | 1.0989 |
| net_win_rate | 0.5455 |
| gross_profit_factor | 1.1900 |
| gross_win_rate | 0.5455 |
| sharpe_ratio | 0.1070 |
| sortino_ratio | 0.0051 |
| max_drawdown | 0.0313 |
| cagr | 0.0020 |
| net_avg_win | 94.3077 |
| net_avg_loss | -102.9799 |
| avg_hold_time_bars | 4.3636 |
| exposure | 0.0022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
