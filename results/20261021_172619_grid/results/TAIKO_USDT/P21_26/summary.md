# EMA Hourly Continuation — TAIKO/USDT P21_26

**Symbol:** TAIKO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 187 |
| net_profit_factor | 0.7999 |
| net_win_rate | 0.5508 |
| gross_profit_factor | 1.2087 |
| gross_win_rate | 0.5508 |
| sharpe_ratio | -0.9333 |
| sortino_ratio | -0.1901 |
| max_drawdown | 0.2726 |
| cagr | -0.0835 |
| net_avg_win | 72.6297 |
| net_avg_loss | -111.3422 |
| avg_hold_time_bars | 6.3155 |
| exposure | 0.0567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
