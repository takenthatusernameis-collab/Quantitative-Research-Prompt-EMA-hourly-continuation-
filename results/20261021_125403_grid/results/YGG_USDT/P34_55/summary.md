# EMA Hourly Continuation — YGG/USDT P34_55

**Symbol:** YGG/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6812 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9263 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -2.3100 |
| sortino_ratio | -0.6474 |
| max_drawdown | 0.5286 |
| cagr | -0.2561 |
| net_avg_win | 60.0705 |
| net_avg_loss | -83.2896 |
| avg_hold_time_bars | 5.5221 |
| exposure | 0.0962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
