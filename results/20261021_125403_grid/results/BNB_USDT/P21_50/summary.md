# EMA Hourly Continuation — BNB/USDT P21_50

**Symbol:** BNB/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.5969 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0516 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -3.3858 |
| sortino_ratio | -1.0104 |
| max_drawdown | 0.6925 |
| cagr | -0.3697 |
| net_avg_win | 46.8297 |
| net_avg_loss | -81.4592 |
| avg_hold_time_bars | 7.4906 |
| exposure | 0.1450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
