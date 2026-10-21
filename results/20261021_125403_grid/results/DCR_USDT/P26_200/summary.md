# EMA Hourly Continuation — DCR/USDT P26_200

**Symbol:** DCR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.7687 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 0.9705 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -1.6085 |
| sortino_ratio | -0.4552 |
| max_drawdown | 0.4623 |
| cagr | -0.1898 |
| net_avg_win | 70.5893 |
| net_avg_loss | -88.6295 |
| avg_hold_time_bars | 28.4835 |
| exposure | 0.5091 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
