# EMA Hourly Continuation — MOCA/USDT P21_200

**Symbol:** MOCA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.5741 |
| net_win_rate | 0.4415 |
| gross_profit_factor | 0.8200 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -3.5095 |
| sortino_ratio | -0.9557 |
| max_drawdown | 0.6550 |
| cagr | -0.3700 |
| net_avg_win | 58.0871 |
| net_avg_loss | -79.9964 |
| avg_hold_time_bars | 36.1667 |
| exposure | 0.6201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
