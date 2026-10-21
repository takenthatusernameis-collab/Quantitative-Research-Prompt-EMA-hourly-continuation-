# EMA Hourly Continuation — AERO/USDT P8_89

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 1.0172 |
| net_win_rate | 0.5453 |
| gross_profit_factor | 1.1806 |
| gross_win_rate | 0.5453 |
| sharpe_ratio | 0.2065 |
| sortino_ratio | 0.0674 |
| max_drawdown | 0.2311 |
| cagr | 0.0194 |
| net_avg_win | 105.6212 |
| net_avg_loss | -124.5115 |
| avg_hold_time_bars | 26.9724 |
| exposure | 0.6228 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
