# EMA Hourly Continuation — ARB/USDT P100_200

**Symbol:** ARB/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.5794 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9566 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -3.0499 |
| sortino_ratio | -0.8148 |
| max_drawdown | 0.6300 |
| cagr | -0.3231 |
| net_avg_win | 48.8849 |
| net_avg_loss | -81.5960 |
| avg_hold_time_bars | 9.1034 |
| exposure | 0.1481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
