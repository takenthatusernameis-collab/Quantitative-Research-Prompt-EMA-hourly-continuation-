# EMA Hourly Continuation — W/USDT P8_200

**Symbol:** W/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 1.0402 |
| net_win_rate | 0.5418 |
| gross_profit_factor | 1.1785 |
| gross_win_rate | 0.5418 |
| sharpe_ratio | 0.2654 |
| sortino_ratio | 0.0665 |
| max_drawdown | 0.1500 |
| cagr | 0.0233 |
| net_avg_win | 94.9513 |
| net_avg_loss | -107.9407 |
| avg_hold_time_bars | 57.7124 |
| exposure | 0.7844 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
