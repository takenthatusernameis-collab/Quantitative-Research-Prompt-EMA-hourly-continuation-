# EMA Hourly Continuation — COTI/USDT P26_144

**Symbol:** COTI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.9306 |
| net_win_rate | 0.5306 |
| gross_profit_factor | 1.1158 |
| gross_win_rate | 0.5306 |
| sharpe_ratio | -0.3730 |
| sortino_ratio | -0.1066 |
| max_drawdown | 0.2998 |
| cagr | -0.0530 |
| net_avg_win | 82.3212 |
| net_avg_loss | -100.0011 |
| avg_hold_time_bars | 25.8444 |
| exposure | 0.4605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
