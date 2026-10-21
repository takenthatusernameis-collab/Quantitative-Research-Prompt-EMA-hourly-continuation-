# EMA Hourly Continuation — BDX/USDT P144_200

**Symbol:** BDX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 177 |
| net_profit_factor | 0.3995 |
| net_win_rate | 0.4237 |
| gross_profit_factor | 0.6879 |
| gross_win_rate | 0.4237 |
| sharpe_ratio | -3.4052 |
| sortino_ratio | -0.6530 |
| max_drawdown | 0.5495 |
| cagr | -0.2603 |
| net_avg_win | 47.1027 |
| net_avg_loss | -86.6911 |
| avg_hold_time_bars | 6.9492 |
| exposure | 0.0559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
