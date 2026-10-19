# EMA Hourly Continuation — KCS/USDT P12_26

**Symbol:** KCS/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1360 |
| net_profit_factor | 0.1211 |
| net_win_rate | 0.2596 |
| gross_profit_factor | 0.5381 |
| gross_win_rate | 0.3559 |
| sharpe_ratio | -20.2991 |
| sortino_ratio | -11.5716 |
| max_drawdown | 1.0000 |
| cagr | -0.9984 |
| net_avg_win | 3.9040 |
| net_avg_loss | -11.2990 |
| avg_hold_time_bars | 3.3662 |
| exposure | 0.2081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
