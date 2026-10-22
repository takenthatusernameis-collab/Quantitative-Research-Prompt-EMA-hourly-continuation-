# EMA Hourly Continuation — FLUX/USDT P100_144

**Symbol:** FLUX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.8643 |
| net_win_rate | 0.5437 |
| gross_profit_factor | 1.1667 |
| gross_win_rate | 0.5437 |
| sharpe_ratio | -0.6198 |
| sortino_ratio | -0.1426 |
| max_drawdown | 0.2397 |
| cagr | -0.0651 |
| net_avg_win | 72.3063 |
| net_avg_loss | -99.6634 |
| avg_hold_time_bars | 6.1548 |
| exposure | 0.0705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
