# EMA Hourly Continuation — TRB/USDT P55_89

**Symbol:** TRB/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 728 |
| net_profit_factor | 0.4419 |
| net_win_rate | 0.4396 |
| gross_profit_factor | 0.8517 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -7.0589 |
| sortino_ratio | -2.6847 |
| max_drawdown | 0.9657 |
| cagr | -0.7349 |
| net_avg_win | 23.8761 |
| net_avg_loss | -42.3752 |
| avg_hold_time_bars | 4.2624 |
| exposure | 0.1404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
