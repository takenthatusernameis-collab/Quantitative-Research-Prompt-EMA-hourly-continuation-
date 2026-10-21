# EMA Hourly Continuation — BONK/USDT P20_200

**Symbol:** BONK/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 1.0314 |
| net_win_rate | 0.5442 |
| gross_profit_factor | 1.1875 |
| gross_win_rate | 0.5476 |
| sharpe_ratio | 0.2231 |
| sortino_ratio | 0.0554 |
| max_drawdown | 0.2052 |
| cagr | 0.0184 |
| net_avg_win | 96.3030 |
| net_avg_loss | -111.4861 |
| avg_hold_time_bars | 45.6429 |
| exposure | 0.6100 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
