# EMA Hourly Continuation — GALA/USDT P12_144

**Symbol:** GALA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.7136 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9633 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -2.0372 |
| sortino_ratio | -0.5659 |
| max_drawdown | 0.5047 |
| cagr | -0.2346 |
| net_avg_win | 64.4643 |
| net_avg_loss | -87.1158 |
| avg_hold_time_bars | 41.7273 |
| exposure | 0.7302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
