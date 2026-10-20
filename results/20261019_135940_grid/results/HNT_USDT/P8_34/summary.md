# EMA Hourly Continuation — HNT/USDT P8_34

**Symbol:** HNT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1412 |
| net_profit_factor | 0.4221 |
| net_win_rate | 0.4164 |
| gross_profit_factor | 0.7089 |
| gross_win_rate | 0.4263 |
| sharpe_ratio | -9.5784 |
| sortino_ratio | -5.0415 |
| max_drawdown | 0.9981 |
| cagr | -0.9165 |
| net_avg_win | 12.3975 |
| net_avg_loss | -20.9589 |
| avg_hold_time_bars | 5.4880 |
| exposure | 0.3522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
