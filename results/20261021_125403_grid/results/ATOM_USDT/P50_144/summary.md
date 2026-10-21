# EMA Hourly Continuation — ATOM/USDT P50_144

**Symbol:** ATOM/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.8261 |
| net_win_rate | 0.5242 |
| gross_profit_factor | 1.0791 |
| gross_win_rate | 0.5242 |
| sharpe_ratio | -0.9641 |
| sortino_ratio | -0.2524 |
| max_drawdown | 0.2908 |
| cagr | -0.1110 |
| net_avg_win | 70.2579 |
| net_avg_loss | -93.7152 |
| avg_hold_time_bars | 16.2424 |
| exposure | 0.2436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
