# EMA Hourly Continuation — RENDER/USDT P8_21

**Symbol:** RENDER/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1425 |
| net_profit_factor | 0.5304 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.9646 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -9.7599 |
| sortino_ratio | -5.5543 |
| max_drawdown | 0.9979 |
| cagr | -0.9393 |
| net_avg_win | 17.0735 |
| net_avg_loss | -27.7714 |
| avg_hold_time_bars | 2.9396 |
| exposure | 0.2211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
