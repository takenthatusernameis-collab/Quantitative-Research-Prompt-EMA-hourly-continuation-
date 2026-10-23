# EMA Hourly Continuation — DIA/USDT P50_89

**Symbol:** DIA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.5985 |
| net_win_rate | 0.4899 |
| gross_profit_factor | 1.0463 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -4.5837 |
| sortino_ratio | -1.6987 |
| max_drawdown | 0.8759 |
| cagr | -0.5565 |
| net_avg_win | 38.3254 |
| net_avg_loss | -61.4913 |
| avg_hold_time_bars | 4.8873 |
| exposure | 0.1530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
