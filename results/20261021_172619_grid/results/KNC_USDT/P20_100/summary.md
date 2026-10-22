# EMA Hourly Continuation — KNC/USDT P20_100

**Symbol:** KNC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.7297 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9759 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -2.8273 |
| sortino_ratio | -0.9106 |
| max_drawdown | 0.7154 |
| cagr | -0.3427 |
| net_avg_win | 72.0705 |
| net_avg_loss | -90.5972 |
| avg_hold_time_bars | 19.5353 |
| exposure | 0.4529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
