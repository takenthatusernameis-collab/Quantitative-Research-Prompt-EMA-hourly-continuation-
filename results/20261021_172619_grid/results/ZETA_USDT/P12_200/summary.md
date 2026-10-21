# EMA Hourly Continuation — ZETA/USDT P12_200

**Symbol:** ZETA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.8980 |
| net_win_rate | 0.5132 |
| gross_profit_factor | 1.0543 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -0.4758 |
| sortino_ratio | -0.1029 |
| max_drawdown | 0.2104 |
| cagr | -0.0485 |
| net_avg_win | 88.7498 |
| net_avg_loss | -104.1672 |
| avg_hold_time_bars | 75.5219 |
| exposure | 0.7792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
