# EMA Hourly Continuation — CFX/USDT P20_34

**Symbol:** CFX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.6402 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.8968 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -2.3891 |
| sortino_ratio | -0.6059 |
| max_drawdown | 0.5544 |
| cagr | -0.2418 |
| net_avg_win | 59.4141 |
| net_avg_loss | -85.4097 |
| avg_hold_time_bars | 5.8978 |
| exposure | 0.0839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
