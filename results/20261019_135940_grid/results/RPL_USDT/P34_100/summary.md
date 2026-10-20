# EMA Hourly Continuation — RPL/USDT P34_100

**Symbol:** RPL/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.6582 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9601 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -3.3022 |
| sortino_ratio | -1.1336 |
| max_drawdown | 0.7418 |
| cagr | -0.4116 |
| net_avg_win | 50.3739 |
| net_avg_loss | -69.8429 |
| avg_hold_time_bars | 12.5347 |
| exposure | 0.3352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
