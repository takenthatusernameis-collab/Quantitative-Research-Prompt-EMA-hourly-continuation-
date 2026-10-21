# EMA Hourly Continuation — MASK/USDT P12_100

**Symbol:** MASK/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.5649 |
| net_win_rate | 0.4434 |
| gross_profit_factor | 0.7594 |
| gross_win_rate | 0.4453 |
| sharpe_ratio | -3.7545 |
| sortino_ratio | -1.2135 |
| max_drawdown | 0.7646 |
| cagr | -0.4313 |
| net_avg_win | 42.5845 |
| net_avg_loss | -60.0473 |
| avg_hold_time_bars | 24.4914 |
| exposure | 0.5800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
