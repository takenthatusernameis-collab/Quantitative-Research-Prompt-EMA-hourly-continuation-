# EMA Hourly Continuation — SAFE/USDT P12_144

**Symbol:** SAFE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.6138 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.8495 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -3.0705 |
| sortino_ratio | -0.9566 |
| max_drawdown | 0.6909 |
| cagr | -0.3681 |
| net_avg_win | 46.8817 |
| net_avg_loss | -67.6050 |
| avg_hold_time_bars | 29.8923 |
| exposure | 0.6735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
