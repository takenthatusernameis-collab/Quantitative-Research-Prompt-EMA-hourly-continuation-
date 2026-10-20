# EMA Hourly Continuation — EWT/USDT P34_55

**Symbol:** EWT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.3810 |
| net_win_rate | 0.4038 |
| gross_profit_factor | 0.7698 |
| gross_win_rate | 0.4186 |
| sharpe_ratio | -8.5532 |
| sortino_ratio | -3.2865 |
| max_drawdown | 0.9857 |
| cagr | -0.8149 |
| net_avg_win | 20.2246 |
| net_avg_loss | -35.9432 |
| avg_hold_time_bars | 4.1723 |
| exposure | 0.1409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
