# EMA Hourly Continuation — AAVE/USDT P34_144

**Symbol:** AAVE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6425 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 1.0248 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -3.1788 |
| sortino_ratio | -1.0172 |
| max_drawdown | 0.7381 |
| cagr | -0.3928 |
| net_avg_win | 49.1894 |
| net_avg_loss | -75.9765 |
| avg_hold_time_bars | 15.4389 |
| exposure | 0.3677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
