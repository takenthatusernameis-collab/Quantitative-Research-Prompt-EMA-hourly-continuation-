# EMA Hourly Continuation — ZRO/USDT P144_200

**Symbol:** ZRO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 181 |
| net_profit_factor | 0.7560 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9519 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -1.1530 |
| sortino_ratio | -0.2304 |
| max_drawdown | 0.2781 |
| cagr | -0.1007 |
| net_avg_win | 76.3194 |
| net_avg_loss | -97.6625 |
| avg_hold_time_bars | 5.2983 |
| exposure | 0.0469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
