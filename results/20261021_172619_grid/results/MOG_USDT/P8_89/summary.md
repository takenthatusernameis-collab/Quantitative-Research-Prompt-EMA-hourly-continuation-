# EMA Hourly Continuation — MOG/USDT P8_89

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.8612 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9855 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -1.1038 |
| sortino_ratio | -0.3542 |
| max_drawdown | 0.4320 |
| cagr | -0.1538 |
| net_avg_win | 86.2726 |
| net_avg_loss | -98.8837 |
| avg_hold_time_bars | 27.0889 |
| exposure | 0.6208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
