# EMA Hourly Continuation — NOT/USDT P26_50

**Symbol:** NOT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.8721 |
| net_win_rate | 0.5312 |
| gross_profit_factor | 1.1264 |
| gross_win_rate | 0.5312 |
| sharpe_ratio | -0.8020 |
| sortino_ratio | -0.2210 |
| max_drawdown | 0.2847 |
| cagr | -0.0987 |
| net_avg_win | 81.4290 |
| net_avg_loss | -105.8171 |
| avg_hold_time_bars | 6.2159 |
| exposure | 0.1028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
