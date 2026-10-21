# EMA Hourly Continuation — MLK/USDT P100_200

**Symbol:** MLK/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.4308 |
| net_win_rate | 0.3636 |
| gross_profit_factor | 0.6025 |
| gross_win_rate | 0.3636 |
| sharpe_ratio | -4.4519 |
| sortino_ratio | -1.0430 |
| max_drawdown | 0.7080 |
| cagr | -0.3862 |
| net_avg_win | 53.5904 |
| net_avg_loss | -71.0827 |
| avg_hold_time_bars | 12.2873 |
| exposure | 0.1529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
