# EMA Hourly Continuation — KMNO/USDT P8_100

**Symbol:** KMNO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.8496 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -1.1150 |
| sortino_ratio | -0.3418 |
| max_drawdown | 0.3400 |
| cagr | -0.1487 |
| net_avg_win | 81.0021 |
| net_avg_loss | -97.9058 |
| avg_hold_time_bars | 31.4735 |
| exposure | 0.6568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
