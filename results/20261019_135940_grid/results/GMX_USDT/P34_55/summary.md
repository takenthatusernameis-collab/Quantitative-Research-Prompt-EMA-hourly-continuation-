# EMA Hourly Continuation — GMX/USDT P34_55

**Symbol:** GMX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 874 |
| net_profit_factor | 0.3591 |
| net_win_rate | 0.3959 |
| gross_profit_factor | 0.7097 |
| gross_win_rate | 0.4142 |
| sharpe_ratio | -9.2545 |
| sortino_ratio | -3.8886 |
| max_drawdown | 0.9923 |
| cagr | -0.8544 |
| net_avg_win | 16.0671 |
| net_avg_loss | -29.3183 |
| avg_hold_time_bars | 3.6453 |
| exposure | 0.1448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
