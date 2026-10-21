# EMA Hourly Continuation — ENA/USDT P8_200

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 1.0244 |
| net_win_rate | 0.5331 |
| gross_profit_factor | 1.1397 |
| gross_win_rate | 0.5331 |
| sharpe_ratio | 0.1644 |
| sortino_ratio | 0.0370 |
| max_drawdown | 0.1271 |
| cagr | 0.0114 |
| net_avg_win | 93.8664 |
| net_avg_loss | -104.6089 |
| avg_hold_time_bars | 74.2231 |
| exposure | 0.8165 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
