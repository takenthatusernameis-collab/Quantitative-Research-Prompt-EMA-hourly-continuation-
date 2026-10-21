# EMA Hourly Continuation — SUSHI/USDT P100_200

**Symbol:** SUSHI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.8243 |
| net_win_rate | 0.5222 |
| gross_profit_factor | 1.0813 |
| gross_win_rate | 0.5222 |
| sharpe_ratio | -0.9353 |
| sortino_ratio | -0.2208 |
| max_drawdown | 0.2534 |
| cagr | -0.0976 |
| net_avg_win | 75.9303 |
| net_avg_loss | -100.6804 |
| avg_hold_time_bars | 11.4963 |
| exposure | 0.1405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
