# EMA Hourly Continuation — AAVE/USDT P21_200

**Symbol:** AAVE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.9719 |
| net_win_rate | 0.5374 |
| gross_profit_factor | 1.1453 |
| gross_win_rate | 0.5374 |
| sharpe_ratio | -0.0920 |
| sortino_ratio | -0.0228 |
| max_drawdown | 0.2055 |
| cagr | -0.0156 |
| net_avg_win | 84.6788 |
| net_avg_loss | -101.2247 |
| avg_hold_time_bars | 46.2789 |
| exposure | 0.6185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
