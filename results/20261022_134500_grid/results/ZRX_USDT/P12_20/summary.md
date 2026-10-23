# EMA Hourly Continuation — ZRX/USDT P12_20

**Symbol:** ZRX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1417 |
| net_profit_factor | 0.3255 |
| net_win_rate | 0.3966 |
| gross_profit_factor | 0.8878 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -13.2182 |
| sortino_ratio | -7.1076 |
| max_drawdown | 0.9999 |
| cagr | -0.9731 |
| net_avg_win | 8.5861 |
| net_avg_loss | -17.3383 |
| avg_hold_time_bars | 2.8589 |
| exposure | 0.1841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
