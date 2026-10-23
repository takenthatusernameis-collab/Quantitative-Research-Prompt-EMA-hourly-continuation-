# EMA Hourly Continuation — ZIL/USDT P20_55

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 978 |
| net_profit_factor | 0.4666 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8612 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -7.3548 |
| sortino_ratio | -3.2555 |
| max_drawdown | 0.9817 |
| cagr | -0.7937 |
| net_avg_win | 19.5961 |
| net_avg_loss | -34.0615 |
| avg_hold_time_bars | 5.2965 |
| exposure | 0.2355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
