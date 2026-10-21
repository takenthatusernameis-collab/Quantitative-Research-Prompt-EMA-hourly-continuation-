# EMA Hourly Continuation — COTI/USDT P20_89

**Symbol:** COTI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.8464 |
| net_win_rate | 0.5076 |
| gross_profit_factor | 1.0366 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -1.2685 |
| sortino_ratio | -0.4182 |
| max_drawdown | 0.4472 |
| cagr | -0.1771 |
| net_avg_win | 79.5625 |
| net_avg_loss | -96.8954 |
| avg_hold_time_bars | 15.0322 |
| exposure | 0.3608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
