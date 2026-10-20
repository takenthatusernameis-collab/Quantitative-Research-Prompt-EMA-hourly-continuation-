# EMA Hourly Continuation — SNX/USDT P144_200

**Symbol:** SNX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.4706 |
| net_win_rate | 0.4179 |
| gross_profit_factor | 0.8440 |
| gross_win_rate | 0.4396 |
| sharpe_ratio | -5.0384 |
| sortino_ratio | -1.4606 |
| max_drawdown | 0.8292 |
| cagr | -0.4985 |
| net_avg_win | 42.3690 |
| net_avg_loss | -64.6337 |
| avg_hold_time_bars | 4.2150 |
| exposure | 0.0790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
