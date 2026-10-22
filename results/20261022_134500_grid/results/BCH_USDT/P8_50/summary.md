# EMA Hourly Continuation — BCH/USDT P8_50

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1071 |
| net_profit_factor | 0.4448 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.8923 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -9.0098 |
| sortino_ratio | -4.1268 |
| max_drawdown | 0.9951 |
| cagr | -0.8788 |
| net_avg_win | 17.3669 |
| net_avg_loss | -29.2835 |
| avg_hold_time_bars | 9.6667 |
| exposure | 0.4706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
