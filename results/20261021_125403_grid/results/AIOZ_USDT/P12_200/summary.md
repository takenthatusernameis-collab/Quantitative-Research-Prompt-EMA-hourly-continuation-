# EMA Hourly Continuation — AIOZ/USDT P12_200

**Symbol:** AIOZ/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.8500 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9833 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -1.0042 |
| sortino_ratio | -0.2727 |
| max_drawdown | 0.3874 |
| cagr | -0.1203 |
| net_avg_win | 87.1229 |
| net_avg_loss | -100.8045 |
| avg_hold_time_bars | 42.6454 |
| exposure | 0.6998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
