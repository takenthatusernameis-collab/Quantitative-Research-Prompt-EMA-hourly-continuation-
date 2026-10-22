# EMA Hourly Continuation — LTC/USDT P12_34

**Symbol:** LTC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1281 |
| net_profit_factor | 0.2912 |
| net_win_rate | 0.4200 |
| gross_profit_factor | 0.8665 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -11.8063 |
| sortino_ratio | -5.9683 |
| max_drawdown | 0.9996 |
| cagr | -0.9564 |
| net_avg_win | 7.6320 |
| net_avg_loss | -18.9801 |
| avg_hold_time_bars | 3.6511 |
| exposure | 0.2126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
