# EMA Hourly Continuation — AAVE/USDT P50_200

**Symbol:** AAVE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.9259 |
| net_win_rate | 0.5309 |
| gross_profit_factor | 1.1183 |
| gross_win_rate | 0.5309 |
| sharpe_ratio | -0.3744 |
| sortino_ratio | -0.0946 |
| max_drawdown | 0.2181 |
| cagr | -0.0462 |
| net_avg_win | 85.8173 |
| net_avg_loss | -104.9109 |
| avg_hold_time_bars | 24.3453 |
| exposure | 0.3397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
