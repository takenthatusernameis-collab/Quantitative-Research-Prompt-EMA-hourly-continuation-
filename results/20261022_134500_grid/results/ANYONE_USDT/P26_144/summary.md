# EMA Hourly Continuation — ANYONE/USDT P26_144

**Symbol:** ANYONE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.6348 |
| net_win_rate | 0.4370 |
| gross_profit_factor | 0.8170 |
| gross_win_rate | 0.4422 |
| sharpe_ratio | -3.1590 |
| sortino_ratio | -0.9189 |
| max_drawdown | 0.6555 |
| cagr | -0.3543 |
| net_avg_win | 64.1865 |
| net_avg_loss | -78.4874 |
| avg_hold_time_bars | 24.7404 |
| exposure | 0.4863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
