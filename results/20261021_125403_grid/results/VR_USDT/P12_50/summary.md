# EMA Hourly Continuation — VR/USDT P12_50

**Symbol:** VR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6762 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.8589 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -2.8023 |
| sortino_ratio | -0.8743 |
| max_drawdown | 0.6439 |
| cagr | -0.3329 |
| net_avg_win | 59.5034 |
| net_avg_loss | -75.8095 |
| avg_hold_time_bars | 14.2645 |
| exposure | 0.3138 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
