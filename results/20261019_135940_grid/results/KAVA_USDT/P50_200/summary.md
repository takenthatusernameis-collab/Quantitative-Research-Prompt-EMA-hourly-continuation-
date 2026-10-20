# EMA Hourly Continuation — KAVA/USDT P50_200

**Symbol:** KAVA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.5448 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.8963 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -4.4015 |
| sortino_ratio | -1.2512 |
| max_drawdown | 0.7923 |
| cagr | -0.4605 |
| net_avg_win | 51.8062 |
| net_avg_loss | -75.2404 |
| avg_hold_time_bars | 23.1117 |
| exposure | 0.4328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
