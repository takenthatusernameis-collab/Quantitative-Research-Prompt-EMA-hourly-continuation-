# EMA Hourly Continuation — KCS/USDT P12_100

**Symbol:** KCS/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.5524 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8864 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -4.3625 |
| sortino_ratio | -1.3543 |
| max_drawdown | 0.8071 |
| cagr | -0.4659 |
| net_avg_win | 46.1701 |
| net_avg_loss | -68.4108 |
| avg_hold_time_bars | 24.9873 |
| exposure | 0.5350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
