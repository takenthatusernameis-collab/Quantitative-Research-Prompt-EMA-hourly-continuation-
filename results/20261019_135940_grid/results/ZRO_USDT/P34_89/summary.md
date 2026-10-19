# EMA Hourly Continuation — ZRO/USDT P34_89

**Symbol:** ZRO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.7047 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0340 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -3.0839 |
| sortino_ratio | -1.1837 |
| max_drawdown | 0.7332 |
| cagr | -0.4302 |
| net_avg_win | 50.8407 |
| net_avg_loss | -72.7788 |
| avg_hold_time_bars | 7.0264 |
| exposure | 0.2349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
