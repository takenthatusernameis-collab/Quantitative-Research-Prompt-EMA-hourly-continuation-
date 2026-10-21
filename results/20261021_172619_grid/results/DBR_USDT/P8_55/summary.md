# EMA Hourly Continuation — DBR/USDT P8_55

**Symbol:** DBR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.7078 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9550 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -3.0644 |
| sortino_ratio | -1.1144 |
| max_drawdown | 0.6700 |
| cagr | -0.3993 |
| net_avg_win | 62.3132 |
| net_avg_loss | -81.1877 |
| avg_hold_time_bars | 15.5356 |
| exposure | 0.4585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
