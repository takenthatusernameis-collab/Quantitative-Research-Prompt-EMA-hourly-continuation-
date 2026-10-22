# EMA Hourly Continuation — SEI/USDT P100_200

**Symbol:** SEI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6177 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9272 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -2.7479 |
| sortino_ratio | -0.7438 |
| max_drawdown | 0.6206 |
| cagr | -0.2956 |
| net_avg_win | 53.7223 |
| net_avg_loss | -80.9871 |
| avg_hold_time_bars | 8.9973 |
| exposure | 0.1493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
