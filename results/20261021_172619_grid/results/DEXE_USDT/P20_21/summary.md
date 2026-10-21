# EMA Hourly Continuation — DEXE/USDT P20_21

**Symbol:** DEXE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 156 |
| net_profit_factor | 0.7154 |
| net_win_rate | 0.5192 |
| gross_profit_factor | 1.0751 |
| gross_win_rate | 0.5192 |
| sharpe_ratio | -1.2346 |
| sortino_ratio | -0.2218 |
| max_drawdown | 0.2580 |
| cagr | -0.0973 |
| net_avg_win | 70.3727 |
| net_avg_loss | -106.2405 |
| avg_hold_time_bars | 16.9872 |
| exposure | 0.1205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
