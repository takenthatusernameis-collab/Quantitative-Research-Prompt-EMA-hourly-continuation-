# EMA Hourly Continuation — PROM/USDT P12_100

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.5212 |
| net_win_rate | 0.4217 |
| gross_profit_factor | 0.8462 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -6.2501 |
| sortino_ratio | -2.3790 |
| max_drawdown | 0.9486 |
| cagr | -0.6898 |
| net_avg_win | 32.7353 |
| net_avg_loss | -45.7929 |
| avg_hold_time_bars | 16.2182 |
| exposure | 0.5507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
