# EMA Hourly Continuation — NMR/USDT P12_50

**Symbol:** NMR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.7246 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9583 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -3.1965 |
| sortino_ratio | -1.2247 |
| max_drawdown | 0.7659 |
| cagr | -0.4302 |
| net_avg_win | 57.3714 |
| net_avg_loss | -73.4567 |
| avg_hold_time_bars | 9.2205 |
| exposure | 0.3022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
