# EMA Hourly Continuation — ARKM/USDT P26_100

**Symbol:** ARKM/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.6289 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.9170 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -3.5934 |
| sortino_ratio | -1.3112 |
| max_drawdown | 0.7916 |
| cagr | -0.4597 |
| net_avg_win | 42.2028 |
| net_avg_loss | -60.7603 |
| avg_hold_time_bars | 11.4346 |
| exposure | 0.3456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
