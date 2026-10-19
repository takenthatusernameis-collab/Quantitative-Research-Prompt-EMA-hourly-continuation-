# EMA Hourly Continuation — ARB/USDT P26_144

**Symbol:** ARB/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.6833 |
| net_win_rate | 0.4883 |
| gross_profit_factor | 0.9876 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -2.6828 |
| sortino_ratio | -0.8227 |
| max_drawdown | 0.6302 |
| cagr | -0.3220 |
| net_avg_win | 58.7014 |
| net_avg_loss | -81.9768 |
| avg_hold_time_bars | 22.6397 |
| exposure | 0.4826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
