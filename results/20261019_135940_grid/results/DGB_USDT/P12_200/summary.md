# EMA Hourly Continuation — DGB/USDT P12_200

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.6319 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.9200 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -3.5329 |
| sortino_ratio | -1.1155 |
| max_drawdown | 0.7593 |
| cagr | -0.4148 |
| net_avg_win | 54.0223 |
| net_avg_loss | -73.0608 |
| avg_hold_time_bars | 30.8784 |
| exposure | 0.7158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
