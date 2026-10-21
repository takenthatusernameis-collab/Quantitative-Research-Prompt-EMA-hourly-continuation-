# EMA Hourly Continuation — LSK/USDT P50_55

**Symbol:** LSK/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.5376 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.9344 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -3.1488 |
| sortino_ratio | -0.7190 |
| max_drawdown | 0.5751 |
| cagr | -0.2848 |
| net_avg_win | 55.1255 |
| net_avg_loss | -93.2260 |
| avg_hold_time_bars | 5.6190 |
| exposure | 0.0644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
