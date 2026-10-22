# EMA Hourly Continuation — TRX/USDT P100_200

**Symbol:** TRX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.2214 |
| net_win_rate | 0.3774 |
| gross_profit_factor | 0.7656 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -7.6037 |
| sortino_ratio | -2.1083 |
| max_drawdown | 0.9424 |
| cagr | -0.6775 |
| net_avg_win | 19.5406 |
| net_avg_loss | -53.5127 |
| avg_hold_time_bars | 8.6226 |
| exposure | 0.1423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
