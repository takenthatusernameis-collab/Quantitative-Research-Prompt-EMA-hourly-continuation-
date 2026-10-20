# EMA Hourly Continuation — PUNDIX/USDT P20_21

**Symbol:** PUNDIX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1227 |
| net_profit_factor | 0.1168 |
| net_win_rate | 0.2698 |
| gross_profit_factor | 0.5588 |
| gross_win_rate | 0.3888 |
| sharpe_ratio | -18.4225 |
| sortino_ratio | -9.8676 |
| max_drawdown | 1.0000 |
| cagr | -0.9958 |
| net_avg_win | 3.9970 |
| net_avg_loss | -12.6373 |
| avg_hold_time_bars | 2.5224 |
| exposure | 0.1407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
