# EMA Hourly Continuation — XRP/USDT P8_20

**Symbol:** XRP/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.6991 |
| net_win_rate | 0.5290 |
| gross_profit_factor | 1.0954 |
| gross_win_rate | 0.5290 |
| sharpe_ratio | -2.0365 |
| sortino_ratio | -0.5864 |
| max_drawdown | 0.5211 |
| cagr | -0.2346 |
| net_avg_win | 54.0915 |
| net_avg_loss | -86.8932 |
| avg_hold_time_bars | 5.4912 |
| exposure | 0.0991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
