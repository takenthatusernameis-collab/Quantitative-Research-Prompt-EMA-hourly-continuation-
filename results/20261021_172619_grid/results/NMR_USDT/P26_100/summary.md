# EMA Hourly Continuation — NMR/USDT P26_100

**Symbol:** NMR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.7647 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9856 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -2.2275 |
| sortino_ratio | -0.7153 |
| max_drawdown | 0.6283 |
| cagr | -0.2798 |
| net_avg_win | 73.8911 |
| net_avg_loss | -92.1451 |
| avg_hold_time_bars | 15.9960 |
| exposure | 0.3679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
