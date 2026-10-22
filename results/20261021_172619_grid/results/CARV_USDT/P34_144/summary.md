# EMA Hourly Continuation — CARV/USDT P34_144

**Symbol:** CARV/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.6924 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.8807 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -2.2088 |
| sortino_ratio | -0.6028 |
| max_drawdown | 0.4528 |
| cagr | -0.2412 |
| net_avg_win | 69.4123 |
| net_avg_loss | -88.1982 |
| avg_hold_time_bars | 20.7037 |
| exposure | 0.3460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
