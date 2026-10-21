# EMA Hourly Continuation — DEEP/USDT P21_144

**Symbol:** DEEP/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.8996 |
| net_win_rate | 0.5077 |
| gross_profit_factor | 1.0195 |
| gross_win_rate | 0.5077 |
| sharpe_ratio | -0.5631 |
| sortino_ratio | -0.1451 |
| max_drawdown | 0.1696 |
| cagr | -0.0680 |
| net_avg_win | 89.8371 |
| net_avg_loss | -102.9802 |
| avg_hold_time_bars | 39.0846 |
| exposure | 0.5754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
