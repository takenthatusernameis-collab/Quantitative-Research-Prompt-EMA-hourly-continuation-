# EMA Hourly Continuation — DIA/USDT P20_55

**Symbol:** DIA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 938 |
| net_profit_factor | 0.4772 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.7977 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -7.0387 |
| sortino_ratio | -3.0194 |
| max_drawdown | 0.9760 |
| cagr | -0.7704 |
| net_avg_win | 21.8824 |
| net_avg_loss | -35.1446 |
| avg_hold_time_bars | 5.8881 |
| exposure | 0.2499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
