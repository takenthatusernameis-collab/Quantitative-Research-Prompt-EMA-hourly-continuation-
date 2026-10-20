# EMA Hourly Continuation — DEGEN/USDT P8_12

**Symbol:** DEGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1744 |
| net_profit_factor | 0.3506 |
| net_win_rate | 0.3796 |
| gross_profit_factor | 0.7139 |
| gross_win_rate | 0.4169 |
| sharpe_ratio | -14.9375 |
| sortino_ratio | -8.8640 |
| max_drawdown | 1.0000 |
| cagr | -0.9897 |
| net_avg_win | 8.1568 |
| net_avg_loss | -14.2326 |
| avg_hold_time_bars | 2.0252 |
| exposure | 0.1608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
