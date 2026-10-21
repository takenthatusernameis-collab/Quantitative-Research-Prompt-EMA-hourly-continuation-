# EMA Hourly Continuation — ZETA/USDT P21_26

**Symbol:** ZETA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.6344 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9499 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -2.1014 |
| sortino_ratio | -0.4628 |
| max_drawdown | 0.4206 |
| cagr | -0.1891 |
| net_avg_win | 61.4263 |
| net_avg_loss | -93.5996 |
| avg_hold_time_bars | 4.4322 |
| exposure | 0.0473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
