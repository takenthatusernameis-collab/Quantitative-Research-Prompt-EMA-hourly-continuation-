# EMA Hourly Continuation — PEPE/USDT P89_200

**Symbol:** PEPE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.7257 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.8923 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -1.6743 |
| sortino_ratio | -0.3925 |
| max_drawdown | 0.3762 |
| cagr | -0.1655 |
| net_avg_win | 75.4786 |
| net_avg_loss | -93.1014 |
| avg_hold_time_bars | 16.2583 |
| exposure | 0.2003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
