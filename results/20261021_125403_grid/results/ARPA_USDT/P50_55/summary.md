# EMA Hourly Continuation — ARPA/USDT P50_55

**Symbol:** ARPA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.5210 |
| net_win_rate | 0.4493 |
| gross_profit_factor | 0.8608 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -3.1945 |
| sortino_ratio | -0.6904 |
| max_drawdown | 0.5584 |
| cagr | -0.2720 |
| net_avg_win | 58.7533 |
| net_avg_loss | -92.0249 |
| avg_hold_time_bars | 5.1718 |
| exposure | 0.0531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
