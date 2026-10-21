# EMA Hourly Continuation — MEW/USDT P26_200

**Symbol:** MEW/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.8039 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9490 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -1.2154 |
| sortino_ratio | -0.3182 |
| max_drawdown | 0.3726 |
| cagr | -0.1376 |
| net_avg_win | 77.1378 |
| net_avg_loss | -92.0485 |
| avg_hold_time_bars | 33.6320 |
| exposure | 0.5152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
