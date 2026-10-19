# EMA Hourly Continuation — THETA/USDT P20_144

**Symbol:** THETA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.6678 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9517 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -2.7511 |
| sortino_ratio | -0.8738 |
| max_drawdown | 0.6600 |
| cagr | -0.3404 |
| net_avg_win | 52.5520 |
| net_avg_loss | -75.0596 |
| avg_hold_time_bars | 22.6949 |
| exposure | 0.5240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
