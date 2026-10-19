# EMA Hourly Continuation — OP/USDT P12_50

**Symbol:** OP/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1055 |
| net_profit_factor | 0.5577 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.9511 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -6.3661 |
| sortino_ratio | -2.9113 |
| max_drawdown | 0.9739 |
| cagr | -0.7541 |
| net_avg_win | 24.9738 |
| net_avg_loss | -38.8355 |
| avg_hold_time_bars | 7.3071 |
| exposure | 0.3504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
