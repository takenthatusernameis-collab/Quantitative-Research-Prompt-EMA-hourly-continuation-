# EMA Hourly Continuation — JST/USDT P26_55

**Symbol:** JST/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.4752 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9886 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -4.6444 |
| sortino_ratio | -1.4344 |
| max_drawdown | 0.8196 |
| cagr | -0.4889 |
| net_avg_win | 32.8360 |
| net_avg_loss | -64.7872 |
| avg_hold_time_bars | 7.6108 |
| exposure | 0.1601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
