# EMA Hourly Continuation — RSR/USDT P50_200

**Symbol:** RSR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.7958 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9457 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -1.1291 |
| sortino_ratio | -0.2837 |
| max_drawdown | 0.2973 |
| cagr | -0.1234 |
| net_avg_win | 72.1855 |
| net_avg_loss | -87.8214 |
| avg_hold_time_bars | 27.4951 |
| exposure | 0.3862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
