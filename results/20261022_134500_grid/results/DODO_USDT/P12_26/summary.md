# EMA Hourly Continuation — DODO/USDT P12_26

**Symbol:** DODO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1452 |
| net_profit_factor | 0.4384 |
| net_win_rate | 0.4256 |
| gross_profit_factor | 0.8912 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -10.4563 |
| sortino_ratio | -5.6313 |
| max_drawdown | 0.9991 |
| cagr | -0.9371 |
| net_avg_win | 12.6183 |
| net_avg_loss | -21.3295 |
| avg_hold_time_bars | 3.1501 |
| exposure | 0.2070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
