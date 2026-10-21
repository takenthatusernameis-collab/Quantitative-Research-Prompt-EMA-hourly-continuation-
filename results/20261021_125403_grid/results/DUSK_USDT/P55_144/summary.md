# EMA Hourly Continuation — DUSK/USDT P55_144

**Symbol:** DUSK/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7974 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 0.9685 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -1.2553 |
| sortino_ratio | -0.3384 |
| max_drawdown | 0.3527 |
| cagr | -0.1453 |
| net_avg_win | 72.8625 |
| net_avg_loss | -89.3479 |
| avg_hold_time_bars | 15.2135 |
| exposure | 0.2462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
