# EMA Hourly Continuation — HTX/USDT P20_89

**Symbol:** HTX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 807 |
| net_profit_factor | 0.3070 |
| net_win_rate | 0.3371 |
| gross_profit_factor | 0.7545 |
| gross_win_rate | 0.3965 |
| sharpe_ratio | -11.6734 |
| sortino_ratio | -4.7943 |
| max_drawdown | 0.9984 |
| cagr | -0.9225 |
| net_avg_win | 16.2585 |
| net_avg_loss | -26.9281 |
| avg_hold_time_bars | 11.9901 |
| exposure | 0.4379 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
