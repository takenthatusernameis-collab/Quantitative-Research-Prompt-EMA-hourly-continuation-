# EMA Hourly Continuation — ILV/USDT P8_100

**Symbol:** ILV/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.8596 |
| net_win_rate | 0.5131 |
| gross_profit_factor | 1.0499 |
| gross_win_rate | 0.5131 |
| sharpe_ratio | -1.0620 |
| sortino_ratio | -0.3398 |
| max_drawdown | 0.3852 |
| cagr | -0.1477 |
| net_avg_win | 79.3962 |
| net_avg_loss | -97.3242 |
| avg_hold_time_bars | 28.9054 |
| exposure | 0.6530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
