# EMA Hourly Continuation — XTZ/USDT P34_55

**Symbol:** XTZ/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.6195 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9456 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -2.8757 |
| sortino_ratio | -0.7879 |
| max_drawdown | 0.6000 |
| cagr | -0.3012 |
| net_avg_win | 54.9001 |
| net_avg_loss | -83.4024 |
| avg_hold_time_bars | 5.9559 |
| exposure | 0.0983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
