# EMA Hourly Continuation — XTZ/USDT P12_50

**Symbol:** XTZ/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1061 |
| net_profit_factor | 0.4677 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.9399 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -7.3778 |
| sortino_ratio | -3.3756 |
| max_drawdown | 0.9847 |
| cagr | -0.8106 |
| net_avg_win | 17.7683 |
| net_avg_loss | -32.2300 |
| avg_hold_time_bars | 7.4430 |
| exposure | 0.3590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
