# EMA Hourly Continuation — VR/USDT P8_200

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.7304 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.8605 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -2.0860 |
| sortino_ratio | -0.5511 |
| max_drawdown | 0.4996 |
| cagr | -0.2269 |
| net_avg_win | 81.1124 |
| net_avg_loss | -92.9282 |
| avg_hold_time_bars | 44.2751 |
| exposure | 0.7024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
