# EMA Hourly Continuation — SUN/USDT P34_89

**Symbol:** SUN/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.4672 |
| net_win_rate | 0.4130 |
| gross_profit_factor | 0.8046 |
| gross_win_rate | 0.4269 |
| sharpe_ratio | -5.7530 |
| sortino_ratio | -1.7051 |
| max_drawdown | 0.8756 |
| cagr | -0.5595 |
| net_avg_win | 43.0403 |
| net_avg_loss | -64.8106 |
| avg_hold_time_bars | 12.1021 |
| exposure | 0.2360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
