# EMA Hourly Continuation — TWT/USDT P34_89

**Symbol:** TWT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.4858 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.9032 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -6.1343 |
| sortino_ratio | -2.3138 |
| max_drawdown | 0.9456 |
| cagr | -0.6793 |
| net_avg_win | 27.4796 |
| net_avg_loss | -46.8761 |
| avg_hold_time_bars | 7.7762 |
| exposure | 0.2527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
