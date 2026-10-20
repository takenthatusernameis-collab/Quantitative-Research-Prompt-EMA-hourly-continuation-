# EMA Hourly Continuation — NMR/USDT P20_55

**Symbol:** NMR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1023 |
| net_profit_factor | 0.5740 |
| net_win_rate | 0.4516 |
| gross_profit_factor | 0.9829 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -7.4089 |
| sortino_ratio | -3.3152 |
| max_drawdown | 0.9848 |
| cagr | -0.8080 |
| net_avg_win | 28.7036 |
| net_avg_loss | -41.1810 |
| avg_hold_time_bars | 5.4448 |
| exposure | 0.2532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
