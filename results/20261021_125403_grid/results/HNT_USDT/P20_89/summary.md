# EMA Hourly Continuation — HNT/USDT P20_89

**Symbol:** HNT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.8220 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0018 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -1.2329 |
| sortino_ratio | -0.3921 |
| max_drawdown | 0.4275 |
| cagr | -0.1675 |
| net_avg_win | 68.4318 |
| net_avg_loss | -85.3054 |
| avg_hold_time_bars | 16.0569 |
| exposure | 0.3591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
