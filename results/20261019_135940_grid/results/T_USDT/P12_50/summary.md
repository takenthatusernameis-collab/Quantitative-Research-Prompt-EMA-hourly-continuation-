# EMA Hourly Continuation — T/USDT P12_50

**Symbol:** T/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 841 |
| net_profit_factor | 0.5337 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.9164 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -5.8727 |
| sortino_ratio | -2.3842 |
| max_drawdown | 0.9468 |
| cagr | -0.6870 |
| net_avg_win | 28.2868 |
| net_avg_loss | -44.3232 |
| avg_hold_time_bars | 9.4530 |
| exposure | 0.3597 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
