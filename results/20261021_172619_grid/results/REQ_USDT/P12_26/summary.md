# EMA Hourly Continuation — REQ/USDT P12_26

**Symbol:** REQ/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.5161 |
| net_win_rate | 0.4262 |
| gross_profit_factor | 0.8459 |
| gross_win_rate | 0.4262 |
| sharpe_ratio | -6.3347 |
| sortino_ratio | -2.2406 |
| max_drawdown | 0.9291 |
| cagr | -0.6491 |
| net_avg_win | 38.5130 |
| net_avg_loss | -55.4243 |
| avg_hold_time_bars | 5.2604 |
| exposure | 0.1442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
