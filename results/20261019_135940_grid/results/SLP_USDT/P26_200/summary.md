# EMA Hourly Continuation — SLP/USDT P26_200

**Symbol:** SLP/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7061 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 1.0131 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -2.4515 |
| sortino_ratio | -0.7394 |
| max_drawdown | 0.5972 |
| cagr | -0.2948 |
| net_avg_win | 62.6209 |
| net_avg_loss | -86.0026 |
| avg_hold_time_bars | 27.5670 |
| exposure | 0.5701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
