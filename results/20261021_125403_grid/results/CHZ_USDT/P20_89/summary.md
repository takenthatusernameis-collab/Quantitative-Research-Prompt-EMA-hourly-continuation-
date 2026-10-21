# EMA Hourly Continuation — CHZ/USDT P20_89

**Symbol:** CHZ/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.8362 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0562 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -1.2119 |
| sortino_ratio | -0.3750 |
| max_drawdown | 0.3898 |
| cagr | -0.1602 |
| net_avg_win | 76.1593 |
| net_avg_loss | -95.9134 |
| avg_hold_time_bars | 17.7177 |
| exposure | 0.3737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
