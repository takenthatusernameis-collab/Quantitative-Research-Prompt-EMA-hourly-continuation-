# EMA Hourly Continuation — WIN/USDT P8_100

**Symbol:** WIN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7847 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0291 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -1.6027 |
| sortino_ratio | -0.5030 |
| max_drawdown | 0.5084 |
| cagr | -0.2081 |
| net_avg_win | 66.2280 |
| net_avg_loss | -87.6327 |
| avg_hold_time_bars | 29.7244 |
| exposure | 0.6472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
