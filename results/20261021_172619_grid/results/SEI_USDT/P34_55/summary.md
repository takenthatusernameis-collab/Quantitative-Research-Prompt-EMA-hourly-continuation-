# EMA Hourly Continuation — SEI/USDT P34_55

**Symbol:** SEI/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.6558 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.8758 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -2.2141 |
| sortino_ratio | -0.5469 |
| max_drawdown | 0.4721 |
| cagr | -0.2215 |
| net_avg_win | 63.0810 |
| net_avg_loss | -85.8379 |
| avg_hold_time_bars | 5.9398 |
| exposure | 0.0807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
