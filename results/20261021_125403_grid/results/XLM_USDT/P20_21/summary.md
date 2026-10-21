# EMA Hourly Continuation — XLM/USDT P20_21

**Symbol:** XLM/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 109 |
| net_profit_factor | 0.6965 |
| net_win_rate | 0.5229 |
| gross_profit_factor | 1.0957 |
| gross_win_rate | 0.5229 |
| sharpe_ratio | -1.1613 |
| sortino_ratio | -0.1754 |
| max_drawdown | 0.1962 |
| cagr | -0.0769 |
| net_avg_win | 73.2711 |
| net_avg_loss | -115.3094 |
| avg_hold_time_bars | 4.9450 |
| exposure | 0.0245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
