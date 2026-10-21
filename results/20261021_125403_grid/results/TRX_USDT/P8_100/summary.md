# EMA Hourly Continuation — TRX/USDT P8_100

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.6038 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0036 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -3.6359 |
| sortino_ratio | -1.1373 |
| max_drawdown | 0.7404 |
| cagr | -0.4096 |
| net_avg_win | 46.9840 |
| net_avg_loss | -78.1424 |
| avg_hold_time_bars | 29.0779 |
| exposure | 0.6278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
