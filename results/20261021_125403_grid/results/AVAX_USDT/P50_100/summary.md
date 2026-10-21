# EMA Hourly Continuation — AVAX/USDT P50_100

**Symbol:** AVAX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.7619 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -1.6284 |
| sortino_ratio | -0.4247 |
| max_drawdown | 0.4139 |
| cagr | -0.1774 |
| net_avg_win | 74.7116 |
| net_avg_loss | -99.2587 |
| avg_hold_time_bars | 8.4727 |
| exposure | 0.1271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
