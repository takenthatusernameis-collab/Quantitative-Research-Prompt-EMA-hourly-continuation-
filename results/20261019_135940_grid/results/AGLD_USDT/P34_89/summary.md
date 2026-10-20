# EMA Hourly Continuation — AGLD/USDT P34_89

**Symbol:** AGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.6233 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.9649 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -4.5724 |
| sortino_ratio | -1.7172 |
| max_drawdown | 0.8757 |
| cagr | -0.5536 |
| net_avg_win | 43.8495 |
| net_avg_loss | -61.0441 |
| avg_hold_time_bars | 8.1459 |
| exposure | 0.2603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
