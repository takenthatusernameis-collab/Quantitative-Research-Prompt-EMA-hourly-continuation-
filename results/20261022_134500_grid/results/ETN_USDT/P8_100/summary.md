# EMA Hourly Continuation — ETN/USDT P8_100

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 807 |
| net_profit_factor | 0.3957 |
| net_win_rate | 0.3656 |
| gross_profit_factor | 0.5617 |
| gross_win_rate | 0.3804 |
| sharpe_ratio | -8.7717 |
| sortino_ratio | -3.8194 |
| max_drawdown | 0.9800 |
| cagr | -0.8428 |
| net_avg_win | 21.7461 |
| net_avg_loss | -31.6607 |
| avg_hold_time_bars | 12.5725 |
| exposure | 0.5511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
