# EMA Hourly Continuation — SKY/USDT P34_50

**Symbol:** SKY/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.3644 |
| net_win_rate | 0.4415 |
| gross_profit_factor | 0.8424 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -8.7815 |
| sortino_ratio | -3.6989 |
| max_drawdown | 0.9812 |
| cagr | -0.8510 |
| net_avg_win | 17.5003 |
| net_avg_loss | -37.9670 |
| avg_hold_time_bars | 3.3109 |
| exposure | 0.1342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
