# EMA Hourly Continuation — XEC/USDT P55_100

**Symbol:** XEC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.3714 |
| net_win_rate | 0.4234 |
| gross_profit_factor | 0.7154 |
| gross_win_rate | 0.4416 |
| sharpe_ratio | -6.8717 |
| sortino_ratio | -2.4950 |
| max_drawdown | 0.9547 |
| cagr | -0.7047 |
| net_avg_win | 20.2003 |
| net_avg_loss | -39.9341 |
| avg_hold_time_bars | 5.2018 |
| exposure | 0.1551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
