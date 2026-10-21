# EMA Hourly Continuation — BTC/USDT P21_144

**Symbol:** BTC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.7187 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0900 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -1.9311 |
| sortino_ratio | -0.5148 |
| max_drawdown | 0.4979 |
| cagr | -0.2102 |
| net_avg_win | 61.0765 |
| net_avg_loss | -92.6624 |
| avg_hold_time_bars | 31.5547 |
| exposure | 0.4960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
