# EMA Hourly Continuation — INJ/USDT P8_200

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.8887 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 1.0225 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -0.6139 |
| sortino_ratio | -0.1485 |
| max_drawdown | 0.2719 |
| cagr | -0.0687 |
| net_avg_win | 90.7594 |
| net_avg_loss | -104.2967 |
| avg_hold_time_bars | 61.3088 |
| exposure | 0.7942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
