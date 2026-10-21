# EMA Hourly Continuation — GRT/USDT P12_26

**Symbol:** GRT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.6301 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.8692 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -3.3110 |
| sortino_ratio | -1.0135 |
| max_drawdown | 0.7011 |
| cagr | -0.3714 |
| net_avg_win | 55.4465 |
| net_avg_loss | -74.9155 |
| avg_hold_time_bars | 5.4772 |
| exposure | 0.1143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
