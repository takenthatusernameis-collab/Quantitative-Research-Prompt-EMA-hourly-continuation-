# EMA Hourly Continuation — JUP/USDT P12_26

**Symbol:** JUP/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1444 |
| net_profit_factor | 0.4450 |
| net_win_rate | 0.4391 |
| gross_profit_factor | 0.8687 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -10.0462 |
| sortino_ratio | -5.3765 |
| max_drawdown | 0.9988 |
| cagr | -0.9310 |
| net_avg_win | 12.6301 |
| net_avg_loss | -22.2165 |
| avg_hold_time_bars | 2.7015 |
| exposure | 0.1773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
