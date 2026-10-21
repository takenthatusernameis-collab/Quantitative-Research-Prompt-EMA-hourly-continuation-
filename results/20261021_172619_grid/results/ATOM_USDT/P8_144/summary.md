# EMA Hourly Continuation — ATOM/USDT P8_144

**Symbol:** ATOM/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.8951 |
| net_win_rate | 0.5214 |
| gross_profit_factor | 1.0900 |
| gross_win_rate | 0.5214 |
| sharpe_ratio | -0.5174 |
| sortino_ratio | -0.1140 |
| max_drawdown | 0.2668 |
| cagr | -0.0532 |
| net_avg_win | 89.7740 |
| net_avg_loss | -109.2464 |
| avg_hold_time_bars | 77.6239 |
| exposure | 0.8256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
