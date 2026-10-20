# EMA Hourly Continuation — BICO/USDT P26_55

**Symbol:** BICO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 871 |
| net_profit_factor | 0.4311 |
| net_win_rate | 0.4340 |
| gross_profit_factor | 0.7474 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -6.5807 |
| sortino_ratio | -2.7475 |
| max_drawdown | 0.9624 |
| cagr | -0.7285 |
| net_avg_win | 19.2904 |
| net_avg_loss | -34.3066 |
| avg_hold_time_bars | 5.1975 |
| exposure | 0.2058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
