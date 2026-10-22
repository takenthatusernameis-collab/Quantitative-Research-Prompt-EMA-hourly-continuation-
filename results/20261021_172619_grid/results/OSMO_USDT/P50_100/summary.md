# EMA Hourly Continuation — OSMO/USDT P50_100

**Symbol:** OSMO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.6309 |
| net_win_rate | 0.4653 |
| gross_profit_factor | 0.8667 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -2.8454 |
| sortino_ratio | -0.8161 |
| max_drawdown | 0.6168 |
| cagr | -0.3125 |
| net_avg_win | 55.4414 |
| net_avg_loss | -76.4817 |
| avg_hold_time_bars | 9.3069 |
| exposure | 0.1709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
