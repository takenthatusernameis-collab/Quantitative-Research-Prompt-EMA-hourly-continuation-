# EMA Hourly Continuation — BLUR/USDT P8_21

**Symbol:** BLUR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1596 |
| net_profit_factor | 0.4257 |
| net_win_rate | 0.4267 |
| gross_profit_factor | 0.8886 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -11.0028 |
| sortino_ratio | -6.1942 |
| max_drawdown | 0.9996 |
| cagr | -0.9532 |
| net_avg_win | 10.8814 |
| net_avg_loss | -19.0227 |
| avg_hold_time_bars | 3.3352 |
| exposure | 0.2409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
