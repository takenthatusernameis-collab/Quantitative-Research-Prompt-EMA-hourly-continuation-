# EMA Hourly Continuation — TIA/USDT P8_100

**Symbol:** TIA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.9083 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0433 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -0.5713 |
| sortino_ratio | -0.1700 |
| max_drawdown | 0.2631 |
| cagr | -0.0798 |
| net_avg_win | 84.4942 |
| net_avg_loss | -98.3647 |
| avg_hold_time_bars | 35.0651 |
| exposure | 0.6854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
