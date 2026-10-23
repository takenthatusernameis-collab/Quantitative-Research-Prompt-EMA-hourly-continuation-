# EMA Hourly Continuation — POPCAT/USDT P8_21

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1458 |
| net_profit_factor | 0.5280 |
| net_win_rate | 0.4376 |
| gross_profit_factor | 0.7893 |
| gross_win_rate | 0.4465 |
| sharpe_ratio | -9.8962 |
| sortino_ratio | -5.7283 |
| max_drawdown | 0.9977 |
| cagr | -0.9394 |
| net_avg_win | 17.4937 |
| net_avg_loss | -25.7776 |
| avg_hold_time_bars | 3.0316 |
| exposure | 0.2335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
