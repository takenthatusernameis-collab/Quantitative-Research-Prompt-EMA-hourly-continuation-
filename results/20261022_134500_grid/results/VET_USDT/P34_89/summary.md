# EMA Hourly Continuation — VET/USDT P34_89

**Symbol:** VET/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.6091 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 1.0498 |
| gross_win_rate | 0.5050 |
| sharpe_ratio | -4.5798 |
| sortino_ratio | -1.7043 |
| max_drawdown | 0.8872 |
| cagr | -0.5599 |
| net_avg_win | 39.7608 |
| net_avg_loss | -62.8875 |
| avg_hold_time_bars | 7.3730 |
| exposure | 0.2336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
