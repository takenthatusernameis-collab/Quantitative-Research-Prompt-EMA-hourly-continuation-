# EMA Hourly Continuation — LPT/USDT P12_34

**Symbol:** LPT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.6973 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.9223 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -3.6825 |
| sortino_ratio | -1.3636 |
| max_drawdown | 0.7969 |
| cagr | -0.4664 |
| net_avg_win | 58.0207 |
| net_avg_loss | -72.8105 |
| avg_hold_time_bars | 6.7170 |
| exposure | 0.2061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
