# EMA Hourly Continuation — ICP/USDT P34_200

**Symbol:** ICP/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.5303 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8317 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -3.9855 |
| sortino_ratio | -1.1226 |
| max_drawdown | 0.7682 |
| cagr | -0.4336 |
| net_avg_win | 45.6438 |
| net_avg_loss | -70.6628 |
| avg_hold_time_bars | 25.4700 |
| exposure | 0.4828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
