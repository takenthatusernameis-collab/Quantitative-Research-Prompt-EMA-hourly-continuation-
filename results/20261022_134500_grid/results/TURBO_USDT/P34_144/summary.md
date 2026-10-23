# EMA Hourly Continuation — TURBO/USDT P34_144

**Symbol:** TURBO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7763 |
| net_win_rate | 0.5058 |
| gross_profit_factor | 1.0461 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -1.9277 |
| sortino_ratio | -0.6244 |
| max_drawdown | 0.4961 |
| cagr | -0.2537 |
| net_avg_win | 72.8838 |
| net_avg_loss | -96.0938 |
| avg_hold_time_bars | 15.8701 |
| exposure | 0.3731 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
