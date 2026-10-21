# EMA Hourly Continuation — ZETA/USDT P100_144

**Symbol:** ZETA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.6408 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.8763 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -2.6185 |
| sortino_ratio | -0.6302 |
| max_drawdown | 0.5474 |
| cagr | -0.2518 |
| net_avg_win | 70.6581 |
| net_avg_loss | -93.1943 |
| avg_hold_time_bars | 6.4755 |
| exposure | 0.0838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
