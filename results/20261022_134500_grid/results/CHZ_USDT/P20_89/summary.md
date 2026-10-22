# EMA Hourly Continuation — CHZ/USDT P20_89

**Symbol:** CHZ/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.6150 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9945 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -4.2720 |
| sortino_ratio | -1.5561 |
| max_drawdown | 0.8575 |
| cagr | -0.5310 |
| net_avg_win | 42.0745 |
| net_avg_loss | -62.9542 |
| avg_hold_time_bars | 12.6914 |
| exposure | 0.3888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
