# EMA Hourly Continuation — PUNDIX/USDT P20_200

**Symbol:** PUNDIX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.6449 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9601 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -2.9695 |
| sortino_ratio | -0.8505 |
| max_drawdown | 0.6438 |
| cagr | -0.3351 |
| net_avg_win | 58.8020 |
| net_avg_loss | -83.2021 |
| avg_hold_time_bars | 34.1036 |
| exposure | 0.6433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
