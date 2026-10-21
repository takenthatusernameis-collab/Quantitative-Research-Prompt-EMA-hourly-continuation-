# EMA Hourly Continuation — XEC/USDT P20_26

**Symbol:** XEC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.5921 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9827 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -2.9537 |
| sortino_ratio | -0.7807 |
| max_drawdown | 0.6201 |
| cagr | -0.2993 |
| net_avg_win | 51.4879 |
| net_avg_loss | -85.4199 |
| avg_hold_time_bars | 5.0445 |
| exposure | 0.0769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
