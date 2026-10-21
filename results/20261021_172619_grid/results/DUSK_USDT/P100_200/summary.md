# EMA Hourly Continuation — DUSK/USDT P100_200

**Symbol:** DUSK/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.7965 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 0.9733 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -1.0144 |
| sortino_ratio | -0.2428 |
| max_drawdown | 0.3501 |
| cagr | -0.1070 |
| net_avg_win | 68.6715 |
| net_avg_loss | -87.4609 |
| avg_hold_time_bars | 12.1393 |
| exposure | 0.1545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
