# EMA Hourly Continuation — GTC/USDT P55_144

**Symbol:** GTC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6984 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.8856 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -2.2337 |
| sortino_ratio | -0.6164 |
| max_drawdown | 0.5303 |
| cagr | -0.2472 |
| net_avg_win | 66.7111 |
| net_avg_loss | -84.5331 |
| avg_hold_time_bars | 15.3581 |
| exposure | 0.2632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
