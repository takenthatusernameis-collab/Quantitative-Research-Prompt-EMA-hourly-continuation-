# EMA Hourly Continuation — ETC/USDT P55_89

**Symbol:** ETC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.3566 |
| net_win_rate | 0.4666 |
| gross_profit_factor | 0.8739 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -6.8621 |
| sortino_ratio | -2.4732 |
| max_drawdown | 0.9599 |
| cagr | -0.7197 |
| net_avg_win | 17.3145 |
| net_avg_loss | -42.4660 |
| avg_hold_time_bars | 4.0030 |
| exposure | 0.1197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
