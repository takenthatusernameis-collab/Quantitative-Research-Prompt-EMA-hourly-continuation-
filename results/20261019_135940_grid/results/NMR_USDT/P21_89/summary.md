# EMA Hourly Continuation — NMR/USDT P21_89

**Symbol:** NMR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.6562 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9973 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -4.4208 |
| sortino_ratio | -1.6995 |
| max_drawdown | 0.8786 |
| cagr | -0.5601 |
| net_avg_win | 45.7573 |
| net_avg_loss | -65.0865 |
| avg_hold_time_bars | 11.5212 |
| exposure | 0.3949 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
