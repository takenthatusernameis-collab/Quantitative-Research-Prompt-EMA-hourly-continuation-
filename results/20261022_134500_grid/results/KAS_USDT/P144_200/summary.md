# EMA Hourly Continuation — KAS/USDT P144_200

**Symbol:** KAS/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.3548 |
| net_win_rate | 0.3995 |
| gross_profit_factor | 0.7164 |
| gross_win_rate | 0.4252 |
| sharpe_ratio | -6.3904 |
| sortino_ratio | -1.8875 |
| max_drawdown | 0.9088 |
| cagr | -0.6131 |
| net_avg_win | 29.1975 |
| net_avg_loss | -54.7543 |
| avg_hold_time_bars | 4.0350 |
| exposure | 0.0785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
