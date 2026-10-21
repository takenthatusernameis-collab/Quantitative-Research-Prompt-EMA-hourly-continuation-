# EMA Hourly Continuation — CETUS/USDT P144_200

**Symbol:** CETUS/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 207 |
| net_profit_factor | 0.5537 |
| net_win_rate | 0.4251 |
| gross_profit_factor | 0.7284 |
| gross_win_rate | 0.4251 |
| sharpe_ratio | -2.6274 |
| sortino_ratio | -0.5338 |
| max_drawdown | 0.4655 |
| cagr | -0.2182 |
| net_avg_win | 65.2148 |
| net_avg_loss | -87.0984 |
| avg_hold_time_bars | 6.7923 |
| exposure | 0.0636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
