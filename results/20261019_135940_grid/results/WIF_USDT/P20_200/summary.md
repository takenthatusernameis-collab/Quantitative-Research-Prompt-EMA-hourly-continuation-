# EMA Hourly Continuation — WIF/USDT P20_200

**Symbol:** WIF/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.6200 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.8068 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -2.8492 |
| sortino_ratio | -0.7690 |
| max_drawdown | 0.6087 |
| cagr | -0.3058 |
| net_avg_win | 59.3574 |
| net_avg_loss | -76.6792 |
| avg_hold_time_bars | 38.6496 |
| exposure | 0.6518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
