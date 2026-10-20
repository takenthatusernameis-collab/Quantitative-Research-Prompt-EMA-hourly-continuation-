# EMA Hourly Continuation — PUFFER/USDT P20_55

**Symbol:** PUFFER/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.6766 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0278 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -3.6167 |
| sortino_ratio | -1.5192 |
| max_drawdown | 0.7702 |
| cagr | -0.5155 |
| net_avg_win | 45.0180 |
| net_avg_loss | -67.2878 |
| avg_hold_time_bars | 6.3380 |
| exposure | 0.2547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
