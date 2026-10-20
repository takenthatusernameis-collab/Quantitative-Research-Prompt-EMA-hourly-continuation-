# EMA Hourly Continuation — ZETA/USDT P8_34

**Symbol:** ZETA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1274 |
| net_profit_factor | 0.5012 |
| net_win_rate | 0.4435 |
| gross_profit_factor | 0.8419 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -7.7248 |
| sortino_ratio | -3.8809 |
| max_drawdown | 0.9912 |
| cagr | -0.8462 |
| net_avg_win | 17.6264 |
| net_avg_loss | -28.0254 |
| avg_hold_time_bars | 6.5612 |
| exposure | 0.3783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
