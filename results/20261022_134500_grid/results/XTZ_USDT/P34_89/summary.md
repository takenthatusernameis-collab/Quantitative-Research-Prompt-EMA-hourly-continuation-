# EMA Hourly Continuation — XTZ/USDT P34_89

**Symbol:** XTZ/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.5494 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.9901 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -5.2084 |
| sortino_ratio | -1.9612 |
| max_drawdown | 0.9096 |
| cagr | -0.6132 |
| net_avg_win | 32.9478 |
| net_avg_loss | -53.4485 |
| avg_hold_time_bars | 7.9383 |
| exposure | 0.2573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
