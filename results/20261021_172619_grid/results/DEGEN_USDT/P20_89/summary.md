# EMA Hourly Continuation — DEGEN/USDT P20_89

**Symbol:** DEGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.9345 |
| net_win_rate | 0.5250 |
| gross_profit_factor | 1.1050 |
| gross_win_rate | 0.5250 |
| sharpe_ratio | -0.4917 |
| sortino_ratio | -0.1587 |
| max_drawdown | 0.3176 |
| cagr | -0.0765 |
| net_avg_win | 98.0078 |
| net_avg_loss | -115.8997 |
| avg_hold_time_bars | 16.3114 |
| exposure | 0.3721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
