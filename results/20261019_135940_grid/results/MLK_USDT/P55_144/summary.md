# EMA Hourly Continuation — MLK/USDT P55_144

**Symbol:** MLK/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.2703 |
| net_win_rate | 0.2881 |
| gross_profit_factor | 0.4824 |
| gross_win_rate | 0.2938 |
| sharpe_ratio | -10.8622 |
| sortino_ratio | -4.1150 |
| max_drawdown | 0.9948 |
| cagr | -0.8745 |
| net_avg_win | 18.0607 |
| net_avg_loss | -27.0458 |
| avg_hold_time_bars | 7.7359 |
| exposure | 0.2479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
