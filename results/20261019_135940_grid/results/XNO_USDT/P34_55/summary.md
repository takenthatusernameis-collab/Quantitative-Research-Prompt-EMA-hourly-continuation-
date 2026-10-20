# EMA Hourly Continuation — XNO/USDT P34_55

**Symbol:** XNO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1045 |
| net_profit_factor | 0.3994 |
| net_win_rate | 0.3751 |
| gross_profit_factor | 0.8124 |
| gross_win_rate | 0.3952 |
| sharpe_ratio | -11.2368 |
| sortino_ratio | -5.1983 |
| max_drawdown | 0.9986 |
| cagr | -0.9271 |
| net_avg_win | 16.9416 |
| net_avg_loss | -25.4627 |
| avg_hold_time_bars | 2.8689 |
| exposure | 0.1363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
