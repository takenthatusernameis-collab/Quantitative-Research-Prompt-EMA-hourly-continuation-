# EMA Hourly Continuation — CPOOL/USDT P50_200

**Symbol:** CPOOL/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.6628 |
| net_win_rate | 0.4337 |
| gross_profit_factor | 0.7630 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -2.3868 |
| sortino_ratio | -0.6132 |
| max_drawdown | 0.5489 |
| cagr | -0.2471 |
| net_avg_win | 69.5965 |
| net_avg_loss | -80.4231 |
| avg_hold_time_bars | 20.0030 |
| exposure | 0.3019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
