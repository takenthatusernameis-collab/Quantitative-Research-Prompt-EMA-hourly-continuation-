# EMA Hourly Continuation — FLR/USDT P12_89

**Symbol:** FLR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 958 |
| net_profit_factor | 0.5467 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 0.9502 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -6.2918 |
| sortino_ratio | -2.7159 |
| max_drawdown | 0.9671 |
| cagr | -0.7398 |
| net_avg_win | 26.4813 |
| net_avg_loss | -41.1420 |
| avg_hold_time_bars | 11.0470 |
| exposure | 0.4810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
