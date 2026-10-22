# EMA Hourly Continuation — RIO/USDT P34_100

**Symbol:** RIO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.7195 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.8236 |
| gross_win_rate | 0.4447 |
| sharpe_ratio | -2.2855 |
| sortino_ratio | -0.6618 |
| max_drawdown | 0.5760 |
| cagr | -0.2635 |
| net_avg_win | 73.8331 |
| net_avg_loss | -82.1847 |
| avg_hold_time_bars | 11.0000 |
| exposure | 0.2101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
