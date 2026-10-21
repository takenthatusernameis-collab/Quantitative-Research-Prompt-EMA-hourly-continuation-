# EMA Hourly Continuation — SOL/USDT P55_100

**Symbol:** SOL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.6825 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9597 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -2.0354 |
| sortino_ratio | -0.4883 |
| max_drawdown | 0.4442 |
| cagr | -0.2007 |
| net_avg_win | 67.5148 |
| net_avg_loss | -94.7687 |
| avg_hold_time_bars | 8.1679 |
| exposure | 0.1040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
