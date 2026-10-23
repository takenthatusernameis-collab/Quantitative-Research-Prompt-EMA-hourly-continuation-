# EMA Hourly Continuation — ONE/USDT P34_89

**Symbol:** ONE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 745 |
| net_profit_factor | 0.6642 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 1.0157 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -4.7892 |
| sortino_ratio | -1.8458 |
| max_drawdown | 0.8969 |
| cagr | -0.5859 |
| net_avg_win | 50.6255 |
| net_avg_loss | -66.8138 |
| avg_hold_time_bars | 7.0228 |
| exposure | 0.2378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
