# EMA Hourly Continuation — EDU/USDT P21_55

**Symbol:** EDU/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1002 |
| net_profit_factor | 0.4874 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.7666 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -6.3118 |
| sortino_ratio | -2.8192 |
| max_drawdown | 0.9681 |
| cagr | -0.7381 |
| net_avg_win | 20.2272 |
| net_avg_loss | -34.3840 |
| avg_hold_time_bars | 5.4212 |
| exposure | 0.2458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
