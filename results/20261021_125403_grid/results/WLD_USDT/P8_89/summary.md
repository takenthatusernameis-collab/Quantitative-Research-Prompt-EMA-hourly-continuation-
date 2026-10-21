# EMA Hourly Continuation — WLD/USDT P8_89

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 1.0704 |
| net_win_rate | 0.5539 |
| gross_profit_factor | 1.2279 |
| gross_win_rate | 0.5539 |
| sharpe_ratio | 0.5394 |
| sortino_ratio | 0.1724 |
| max_drawdown | 0.2081 |
| cagr | 0.0672 |
| net_avg_win | 100.9726 |
| net_avg_loss | -117.1429 |
| avg_hold_time_bars | 28.5456 |
| exposure | 0.6254 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
