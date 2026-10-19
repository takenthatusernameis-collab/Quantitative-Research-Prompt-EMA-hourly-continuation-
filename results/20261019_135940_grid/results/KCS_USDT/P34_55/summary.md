# EMA Hourly Continuation — KCS/USDT P34_55

**Symbol:** KCS/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 907 |
| net_profit_factor | 0.1435 |
| net_win_rate | 0.2745 |
| gross_profit_factor | 0.6633 |
| gross_win_rate | 0.3815 |
| sharpe_ratio | -15.2977 |
| sortino_ratio | -7.0028 |
| max_drawdown | 0.9999 |
| cagr | -0.9771 |
| net_avg_win | 6.7293 |
| net_avg_loss | -17.7429 |
| avg_hold_time_bars | 3.4906 |
| exposure | 0.1439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
