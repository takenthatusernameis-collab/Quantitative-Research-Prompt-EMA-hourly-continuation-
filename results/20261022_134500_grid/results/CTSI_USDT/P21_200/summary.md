# EMA Hourly Continuation — CTSI/USDT P21_200

**Symbol:** CTSI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7362 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 1.0078 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -1.9262 |
| sortino_ratio | -0.5280 |
| max_drawdown | 0.4856 |
| cagr | -0.2177 |
| net_avg_win | 70.5670 |
| net_avg_loss | -92.3045 |
| avg_hold_time_bars | 39.3908 |
| exposure | 0.6643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
