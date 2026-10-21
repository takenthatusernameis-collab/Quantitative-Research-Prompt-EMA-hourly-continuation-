# EMA Hourly Continuation — JUP/USDT P12_26

**Symbol:** JUP/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.8190 |
| net_win_rate | 0.5194 |
| gross_profit_factor | 1.0780 |
| gross_win_rate | 0.5194 |
| sharpe_ratio | -1.3408 |
| sortino_ratio | -0.4162 |
| max_drawdown | 0.4138 |
| cagr | -0.1748 |
| net_avg_win | 71.8764 |
| net_avg_loss | -94.8461 |
| avg_hold_time_bars | 5.0323 |
| exposure | 0.1061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
