# EMA Hourly Continuation — LPT/USDT P8_100

**Symbol:** LPT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.7558 |
| net_win_rate | 0.4761 |
| gross_profit_factor | 0.9125 |
| gross_win_rate | 0.4761 |
| sharpe_ratio | -1.9981 |
| sortino_ratio | -0.6237 |
| max_drawdown | 0.5510 |
| cagr | -0.2500 |
| net_avg_win | 69.5354 |
| net_avg_loss | -83.6029 |
| avg_hold_time_bars | 30.5904 |
| exposure | 0.6688 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
