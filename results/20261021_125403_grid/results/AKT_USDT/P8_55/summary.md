# EMA Hourly Continuation — AKT/USDT P8_55

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.7945 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9611 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -1.7656 |
| sortino_ratio | -0.6313 |
| max_drawdown | 0.5301 |
| cagr | -0.2537 |
| net_avg_win | 65.3392 |
| net_avg_loss | -79.6522 |
| avg_hold_time_bars | 15.2428 |
| exposure | 0.4337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
