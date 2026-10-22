# EMA Hourly Continuation — PYTH/USDT P21_55

**Symbol:** PYTH/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 920 |
| net_profit_factor | 0.5461 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.9023 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -5.5110 |
| sortino_ratio | -2.3567 |
| max_drawdown | 0.9418 |
| cagr | -0.6764 |
| net_avg_win | 26.4000 |
| net_avg_loss | -42.2352 |
| avg_hold_time_bars | 5.4141 |
| exposure | 0.2264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
