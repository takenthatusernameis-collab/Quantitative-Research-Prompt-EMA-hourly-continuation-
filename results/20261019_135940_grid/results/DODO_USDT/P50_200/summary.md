# EMA Hourly Continuation — DODO/USDT P50_200

**Symbol:** DODO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.5836 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.8263 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -3.6659 |
| sortino_ratio | -1.1144 |
| max_drawdown | 0.7407 |
| cagr | -0.4078 |
| net_avg_win | 49.8910 |
| net_avg_loss | -66.9619 |
| avg_hold_time_bars | 17.1812 |
| exposure | 0.3646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
