# EMA Hourly Continuation — ZRX/USDT P20_21

**Symbol:** ZRX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.5224 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.8463 |
| gross_win_rate | 0.4502 |
| sharpe_ratio | -3.5456 |
| sortino_ratio | -0.8383 |
| max_drawdown | 0.6321 |
| cagr | -0.3229 |
| net_avg_win | 56.4523 |
| net_avg_loss | -87.1680 |
| avg_hold_time_bars | 4.6790 |
| exposure | 0.0576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
