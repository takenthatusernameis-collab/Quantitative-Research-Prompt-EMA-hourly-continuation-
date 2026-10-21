# EMA Hourly Continuation — SNX/USDT P34_100

**Symbol:** SNX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.8823 |
| net_win_rate | 0.5311 |
| gross_profit_factor | 1.1275 |
| gross_win_rate | 0.5311 |
| sharpe_ratio | -0.8111 |
| sortino_ratio | -0.2480 |
| max_drawdown | 0.3413 |
| cagr | -0.1107 |
| net_avg_win | 80.4148 |
| net_avg_loss | -103.2320 |
| avg_hold_time_bars | 12.2844 |
| exposure | 0.2501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
