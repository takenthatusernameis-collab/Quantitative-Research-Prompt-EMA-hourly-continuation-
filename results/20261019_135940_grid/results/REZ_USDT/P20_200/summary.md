# EMA Hourly Continuation — REZ/USDT P20_200

**Symbol:** REZ/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.8865 |
| net_win_rate | 0.5248 |
| gross_profit_factor | 1.1114 |
| gross_win_rate | 0.5272 |
| sharpe_ratio | -0.7673 |
| sortino_ratio | -0.2225 |
| max_drawdown | 0.3032 |
| cagr | -0.1023 |
| net_avg_win | 86.3656 |
| net_avg_loss | -107.5686 |
| avg_hold_time_bars | 32.9059 |
| exposure | 0.6133 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
