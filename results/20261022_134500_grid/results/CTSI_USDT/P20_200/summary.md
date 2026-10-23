# EMA Hourly Continuation — CTSI/USDT P20_200

**Symbol:** CTSI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.7396 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 1.0317 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -1.9748 |
| sortino_ratio | -0.5592 |
| max_drawdown | 0.5022 |
| cagr | -0.2307 |
| net_avg_win | 69.2143 |
| net_avg_loss | -92.1873 |
| avg_hold_time_bars | 35.7619 |
| exposure | 0.6486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
