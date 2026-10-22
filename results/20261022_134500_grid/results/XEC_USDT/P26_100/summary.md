# EMA Hourly Continuation — XEC/USDT P26_100

**Symbol:** XEC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.5933 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9599 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -4.6924 |
| sortino_ratio | -1.7823 |
| max_drawdown | 0.8940 |
| cagr | -0.5717 |
| net_avg_win | 37.5197 |
| net_avg_loss | -56.7848 |
| avg_hold_time_bars | 11.2676 |
| exposure | 0.3697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
