# EMA Hourly Continuation — KSM/USDT P8_34

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1377 |
| net_profit_factor | 0.4465 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8280 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -8.5629 |
| sortino_ratio | -4.4831 |
| max_drawdown | 0.9959 |
| cagr | -0.8867 |
| net_avg_win | 13.0186 |
| net_avg_loss | -23.6714 |
| avg_hold_time_bars | 5.6028 |
| exposure | 0.3507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
