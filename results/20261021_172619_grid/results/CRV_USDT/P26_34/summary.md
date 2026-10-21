# EMA Hourly Continuation — CRV/USDT P26_34

**Symbol:** CRV/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 163 |
| net_profit_factor | 0.6210 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.8574 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -1.8136 |
| sortino_ratio | -0.3308 |
| max_drawdown | 0.3414 |
| cagr | -0.1407 |
| net_avg_win | 68.2727 |
| net_avg_loss | -96.0423 |
| avg_hold_time_bars | 4.4724 |
| exposure | 0.0331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
