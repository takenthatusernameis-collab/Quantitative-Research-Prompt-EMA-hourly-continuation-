# EMA Hourly Continuation — FLIP/USDT P20_100

**Symbol:** FLIP/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.5327 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.8219 |
| gross_win_rate | 0.4544 |
| sharpe_ratio | -4.4703 |
| sortino_ratio | -1.3790 |
| max_drawdown | 0.8150 |
| cagr | -0.4840 |
| net_avg_win | 44.1929 |
| net_avg_loss | -63.5083 |
| avg_hold_time_bars | 21.1535 |
| exposure | 0.4635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
