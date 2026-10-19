# EMA Hourly Continuation — XTZ/USDT P21_89

**Symbol:** XTZ/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.6027 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 1.0138 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -4.4982 |
| sortino_ratio | -1.6724 |
| max_drawdown | 0.8773 |
| cagr | -0.5568 |
| net_avg_win | 39.0581 |
| net_avg_loss | -59.6891 |
| avg_hold_time_bars | 13.2823 |
| exposure | 0.4256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
