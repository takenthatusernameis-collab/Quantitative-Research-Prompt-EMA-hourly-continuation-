# EMA Hourly Continuation — SEI/USDT P50_200

**Symbol:** SEI/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.8053 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9556 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -1.0775 |
| sortino_ratio | -0.2516 |
| max_drawdown | 0.3089 |
| cagr | -0.1102 |
| net_avg_win | 79.6487 |
| net_avg_loss | -95.9984 |
| avg_hold_time_bars | 32.1455 |
| exposure | 0.3916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
