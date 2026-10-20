# EMA Hourly Continuation — CFG/USDT P50_144

**Symbol:** CFG/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.6276 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.8781 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -3.1841 |
| sortino_ratio | -1.0392 |
| max_drawdown | 0.7188 |
| cagr | -0.3898 |
| net_avg_win | 47.3495 |
| net_avg_loss | -66.7369 |
| avg_hold_time_bars | 10.9462 |
| exposure | 0.2682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
