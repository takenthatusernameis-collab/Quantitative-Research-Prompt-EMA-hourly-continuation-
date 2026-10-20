# EMA Hourly Continuation — MINA/USDT P34_200

**Symbol:** MINA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.7974 |
| net_win_rate | 0.5231 |
| gross_profit_factor | 1.1089 |
| gross_win_rate | 0.5323 |
| sharpe_ratio | -1.1384 |
| sortino_ratio | -0.2890 |
| max_drawdown | 0.3640 |
| cagr | -0.1317 |
| net_avg_win | 69.1376 |
| net_avg_loss | -95.0927 |
| avg_hold_time_bars | 38.1169 |
| exposure | 0.5631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
