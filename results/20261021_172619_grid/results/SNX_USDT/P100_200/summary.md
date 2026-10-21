# EMA Hourly Continuation — SNX/USDT P100_200

**Symbol:** SNX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.7536 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9646 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -1.4933 |
| sortino_ratio | -0.3450 |
| max_drawdown | 0.3403 |
| cagr | -0.1470 |
| net_avg_win | 78.9535 |
| net_avg_loss | -100.0721 |
| avg_hold_time_bars | 13.0153 |
| exposure | 0.1543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
