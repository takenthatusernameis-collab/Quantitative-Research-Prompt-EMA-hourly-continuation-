# EMA Hourly Continuation — AZERO/USDT P55_200

**Symbol:** AZERO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.7631 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0230 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -1.6035 |
| sortino_ratio | -0.4255 |
| max_drawdown | 0.4648 |
| cagr | -0.1868 |
| net_avg_win | 72.3444 |
| net_avg_loss | -95.8605 |
| avg_hold_time_bars | 22.7417 |
| exposure | 0.3705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
