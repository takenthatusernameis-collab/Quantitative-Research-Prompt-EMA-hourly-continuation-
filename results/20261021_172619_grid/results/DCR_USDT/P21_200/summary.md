# EMA Hourly Continuation — DCR/USDT P21_200

**Symbol:** DCR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.8344 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.0549 |
| gross_win_rate | 0.5173 |
| sharpe_ratio | -1.0342 |
| sortino_ratio | -0.2974 |
| max_drawdown | 0.3975 |
| cagr | -0.1303 |
| net_avg_win | 71.5563 |
| net_avg_loss | -91.9193 |
| avg_hold_time_bars | 30.6411 |
| exposure | 0.5602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
