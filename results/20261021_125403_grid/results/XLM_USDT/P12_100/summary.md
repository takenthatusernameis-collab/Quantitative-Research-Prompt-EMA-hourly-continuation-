# EMA Hourly Continuation — XLM/USDT P12_100

**Symbol:** XLM/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.8480 |
| net_win_rate | 0.5270 |
| gross_profit_factor | 1.1103 |
| gross_win_rate | 0.5270 |
| sharpe_ratio | -1.0634 |
| sortino_ratio | -0.3365 |
| max_drawdown | 0.3537 |
| cagr | -0.1455 |
| net_avg_win | 71.6745 |
| net_avg_loss | -94.1595 |
| avg_hold_time_bars | 25.4378 |
| exposure | 0.5573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
