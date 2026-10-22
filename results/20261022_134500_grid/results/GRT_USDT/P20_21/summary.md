# EMA Hourly Continuation — GRT/USDT P20_21

**Symbol:** GRT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1211 |
| net_profit_factor | 0.1535 |
| net_win_rate | 0.2808 |
| gross_profit_factor | 0.6198 |
| gross_win_rate | 0.3543 |
| sharpe_ratio | -18.6357 |
| sortino_ratio | -9.9669 |
| max_drawdown | 1.0000 |
| cagr | -0.9965 |
| net_avg_win | 5.3321 |
| net_avg_loss | -13.5625 |
| avg_hold_time_bars | 1.6325 |
| exposure | 0.0895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
