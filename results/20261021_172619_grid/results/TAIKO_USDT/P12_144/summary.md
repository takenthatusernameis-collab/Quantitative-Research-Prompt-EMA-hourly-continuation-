# EMA Hourly Continuation — TAIKO/USDT P12_144

**Symbol:** TAIKO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.9025 |
| net_win_rate | 0.5237 |
| gross_profit_factor | 1.0894 |
| gross_win_rate | 0.5237 |
| sharpe_ratio | -0.5683 |
| sortino_ratio | -0.1546 |
| max_drawdown | 0.2422 |
| cagr | -0.0722 |
| net_avg_win | 85.3132 |
| net_avg_loss | -103.9192 |
| avg_hold_time_bars | 42.4527 |
| exposure | 0.6893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
