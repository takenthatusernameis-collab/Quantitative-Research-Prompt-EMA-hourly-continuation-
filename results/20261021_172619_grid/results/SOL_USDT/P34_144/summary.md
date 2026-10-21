# EMA Hourly Continuation — SOL/USDT P34_144

**Symbol:** SOL/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.7218 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9393 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -1.9438 |
| sortino_ratio | -0.5171 |
| max_drawdown | 0.4747 |
| cagr | -0.2117 |
| net_avg_win | 69.4493 |
| net_avg_loss | -90.3030 |
| avg_hold_time_bars | 21.5476 |
| exposure | 0.3399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
