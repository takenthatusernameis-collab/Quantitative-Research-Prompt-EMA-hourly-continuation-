# EMA Hourly Continuation — EUL/USDT P12_20

**Symbol:** EUL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1415 |
| net_profit_factor | 0.2559 |
| net_win_rate | 0.3753 |
| gross_profit_factor | 0.5494 |
| gross_win_rate | 0.4064 |
| sharpe_ratio | -13.3887 |
| sortino_ratio | -7.1913 |
| max_drawdown | 0.9999 |
| cagr | -0.9740 |
| net_avg_win | 6.4773 |
| net_avg_loss | -15.2018 |
| avg_hold_time_bars | 2.8756 |
| exposure | 0.1850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
