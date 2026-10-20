# EMA Hourly Continuation — ACE/USDT P34_100

**Symbol:** ACE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.7444 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0827 |
| gross_win_rate | 0.5195 |
| sharpe_ratio | -2.0249 |
| sortino_ratio | -0.6556 |
| max_drawdown | 0.5499 |
| cagr | -0.2609 |
| net_avg_win | 59.0782 |
| net_avg_loss | -83.1593 |
| avg_hold_time_bars | 12.1128 |
| exposure | 0.2817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
