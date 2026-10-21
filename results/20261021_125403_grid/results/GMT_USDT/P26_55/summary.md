# EMA Hourly Continuation — GMT/USDT P26_55

**Symbol:** GMT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.6827 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9321 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -2.5453 |
| sortino_ratio | -0.7781 |
| max_drawdown | 0.6111 |
| cagr | -0.2997 |
| net_avg_win | 57.8282 |
| net_avg_loss | -78.9626 |
| avg_hold_time_bars | 7.0154 |
| exposure | 0.1454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
