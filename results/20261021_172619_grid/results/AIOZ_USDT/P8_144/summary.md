# EMA Hourly Continuation — AIOZ/USDT P8_144

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.8481 |
| net_win_rate | 0.4976 |
| gross_profit_factor | 0.9937 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -1.1233 |
| sortino_ratio | -0.3308 |
| max_drawdown | 0.3926 |
| cagr | -0.1438 |
| net_avg_win | 85.4126 |
| net_avg_loss | -99.7681 |
| avg_hold_time_bars | 36.9788 |
| exposure | 0.7127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
