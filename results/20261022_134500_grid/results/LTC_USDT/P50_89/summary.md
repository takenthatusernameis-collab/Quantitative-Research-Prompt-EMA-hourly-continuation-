# EMA Hourly Continuation — LTC/USDT P50_89

**Symbol:** LTC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.2874 |
| net_win_rate | 0.3912 |
| gross_profit_factor | 0.7497 |
| gross_win_rate | 0.4339 |
| sharpe_ratio | -8.8823 |
| sortino_ratio | -3.3659 |
| max_drawdown | 0.9869 |
| cagr | -0.8186 |
| net_avg_win | 14.4651 |
| net_avg_loss | -32.3373 |
| avg_hold_time_bars | 4.5519 |
| exposure | 0.1455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
