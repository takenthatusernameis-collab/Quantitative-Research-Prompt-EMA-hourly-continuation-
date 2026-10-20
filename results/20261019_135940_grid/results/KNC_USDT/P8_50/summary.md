# EMA Hourly Continuation — KNC/USDT P8_50

**Symbol:** KNC/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 952 |
| net_profit_factor | 0.5904 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.9657 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -6.4271 |
| sortino_ratio | -2.7887 |
| max_drawdown | 0.9658 |
| cagr | -0.7393 |
| net_avg_win | 32.9113 |
| net_avg_loss | -44.5741 |
| avg_hold_time_bars | 11.3403 |
| exposure | 0.4907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
