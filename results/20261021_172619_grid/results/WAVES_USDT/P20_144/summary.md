# EMA Hourly Continuation — WAVES/USDT P20_144

**Symbol:** WAVES/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.7640 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 0.9937 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.8403 |
| sortino_ratio | -0.5655 |
| max_drawdown | 0.5239 |
| cagr | -0.2300 |
| net_avg_win | 67.7334 |
| net_avg_loss | -88.2719 |
| avg_hold_time_bars | 24.3753 |
| exposure | 0.5108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
