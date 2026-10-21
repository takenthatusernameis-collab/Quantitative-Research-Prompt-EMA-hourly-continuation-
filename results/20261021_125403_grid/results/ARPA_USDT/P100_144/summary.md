# EMA Hourly Continuation — ARPA/USDT P100_144

**Symbol:** ARPA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.4780 |
| net_win_rate | 0.4088 |
| gross_profit_factor | 0.7045 |
| gross_win_rate | 0.4088 |
| sharpe_ratio | -4.1745 |
| sortino_ratio | -1.0589 |
| max_drawdown | 0.7113 |
| cagr | -0.3869 |
| net_avg_win | 49.9419 |
| net_avg_loss | -72.2421 |
| avg_hold_time_bars | 6.6069 |
| exposure | 0.0951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
