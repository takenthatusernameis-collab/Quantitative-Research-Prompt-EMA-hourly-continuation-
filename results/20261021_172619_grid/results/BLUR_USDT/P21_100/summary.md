# EMA Hourly Continuation — BLUR/USDT P21_100

**Symbol:** BLUR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.9028 |
| net_win_rate | 0.5301 |
| gross_profit_factor | 1.1270 |
| gross_win_rate | 0.5301 |
| sharpe_ratio | -0.7040 |
| sortino_ratio | -0.2144 |
| max_drawdown | 0.3888 |
| cagr | -0.0981 |
| net_avg_win | 89.4522 |
| net_avg_loss | -111.7666 |
| avg_hold_time_bars | 21.7372 |
| exposure | 0.4416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
