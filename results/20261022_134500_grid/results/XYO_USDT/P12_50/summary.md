# EMA Hourly Continuation — XYO/USDT P12_50

**Symbol:** XYO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1190 |
| net_profit_factor | 0.4397 |
| net_win_rate | 0.4084 |
| gross_profit_factor | 0.7832 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -9.6595 |
| sortino_ratio | -4.7111 |
| max_drawdown | 0.9971 |
| cagr | -0.9000 |
| net_avg_win | 16.0983 |
| net_avg_loss | -25.2753 |
| avg_hold_time_bars | 6.7126 |
| exposure | 0.3615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
