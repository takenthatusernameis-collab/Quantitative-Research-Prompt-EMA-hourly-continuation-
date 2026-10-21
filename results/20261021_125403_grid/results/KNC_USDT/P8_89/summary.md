# EMA Hourly Continuation — KNC/USDT P8_89

**Symbol:** KNC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.6920 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.8995 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -2.8663 |
| sortino_ratio | -0.9101 |
| max_drawdown | 0.6699 |
| cagr | -0.3416 |
| net_avg_win | 62.6848 |
| net_avg_loss | -79.6417 |
| avg_hold_time_bars | 29.9719 |
| exposure | 0.6785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
