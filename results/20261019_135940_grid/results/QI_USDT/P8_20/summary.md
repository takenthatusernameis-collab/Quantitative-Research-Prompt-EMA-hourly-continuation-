# EMA Hourly Continuation — QI/USDT P8_20

**Symbol:** QI/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1409 |
| net_profit_factor | 0.3804 |
| net_win_rate | 0.4258 |
| gross_profit_factor | 0.7690 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -10.6496 |
| sortino_ratio | -5.6421 |
| max_drawdown | 0.9992 |
| cagr | -0.9400 |
| net_avg_win | 10.2228 |
| net_avg_loss | -19.9325 |
| avg_hold_time_bars | 3.8943 |
| exposure | 0.2483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
