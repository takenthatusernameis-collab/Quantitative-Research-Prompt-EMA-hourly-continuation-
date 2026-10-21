# EMA Hourly Continuation — SKL/USDT P12_26

**Symbol:** SKL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7631 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.0580 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -2.2782 |
| sortino_ratio | -0.7379 |
| max_drawdown | 0.6351 |
| cagr | -0.2867 |
| net_avg_win | 71.9571 |
| net_avg_loss | -95.7952 |
| avg_hold_time_bars | 5.1929 |
| exposure | 0.1199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
