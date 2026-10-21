# EMA Hourly Continuation — XNO/USDT P12_55

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.6723 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.8646 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -3.6715 |
| sortino_ratio | -1.3617 |
| max_drawdown | 0.8122 |
| cagr | -0.4655 |
| net_avg_win | 52.8022 |
| net_avg_loss | -64.8500 |
| avg_hold_time_bars | 9.5184 |
| exposure | 0.2946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
