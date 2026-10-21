# EMA Hourly Continuation — TURBO/USDT P20_100

**Symbol:** TURBO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.7683 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9189 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -1.9371 |
| sortino_ratio | -0.6106 |
| max_drawdown | 0.5036 |
| cagr | -0.2456 |
| net_avg_win | 75.3641 |
| net_avg_loss | -90.2647 |
| avg_hold_time_bars | 17.9756 |
| exposure | 0.4011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
