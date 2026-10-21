# EMA Hourly Continuation — SOL/USDT P100_200

**Symbol:** SOL/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.6666 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9075 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -2.0070 |
| sortino_ratio | -0.4527 |
| max_drawdown | 0.4267 |
| cagr | -0.1874 |
| net_avg_win | 68.2497 |
| net_avg_loss | -93.7229 |
| avg_hold_time_bars | 13.2731 |
| exposure | 0.1502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
