# EMA Hourly Continuation — ZEN/USDT P50_200

**Symbol:** ZEN/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.6737 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9318 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -2.4331 |
| sortino_ratio | -0.7092 |
| max_drawdown | 0.5910 |
| cagr | -0.2831 |
| net_avg_win | 57.3476 |
| net_avg_loss | -78.9269 |
| avg_hold_time_bars | 20.1722 |
| exposure | 0.3888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
