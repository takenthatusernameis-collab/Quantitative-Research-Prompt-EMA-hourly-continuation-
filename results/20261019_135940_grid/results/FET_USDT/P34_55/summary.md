# EMA Hourly Continuation — FET/USDT P34_55

**Symbol:** FET/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 870 |
| net_profit_factor | 0.3798 |
| net_win_rate | 0.4437 |
| gross_profit_factor | 0.7191 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -7.5976 |
| sortino_ratio | -3.1532 |
| max_drawdown | 0.9808 |
| cagr | -0.7921 |
| net_avg_win | 15.5558 |
| net_avg_loss | -32.6673 |
| avg_hold_time_bars | 2.8276 |
| exposure | 0.1118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
