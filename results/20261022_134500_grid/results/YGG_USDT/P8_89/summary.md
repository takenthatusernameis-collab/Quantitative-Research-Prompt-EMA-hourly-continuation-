# EMA Hourly Continuation — YGG/USDT P8_89

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.7198 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 1.0272 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -3.1171 |
| sortino_ratio | -1.1387 |
| max_drawdown | 0.7734 |
| cagr | -0.4193 |
| net_avg_win | 58.4311 |
| net_avg_loss | -76.2940 |
| avg_hold_time_bars | 21.2688 |
| exposure | 0.6516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
