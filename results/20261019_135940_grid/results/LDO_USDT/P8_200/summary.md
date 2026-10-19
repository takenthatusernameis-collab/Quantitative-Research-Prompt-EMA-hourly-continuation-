# EMA Hourly Continuation — LDO/USDT P8_200

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.6270 |
| net_win_rate | 0.4461 |
| gross_profit_factor | 0.8099 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -2.2277 |
| sortino_ratio | -0.5136 |
| max_drawdown | 0.4778 |
| cagr | -0.2137 |
| net_avg_win | 63.4782 |
| net_avg_loss | -81.5397 |
| avg_hold_time_bars | 69.9517 |
| exposure | 0.8553 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
