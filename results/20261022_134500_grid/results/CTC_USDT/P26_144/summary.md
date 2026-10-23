# EMA Hourly Continuation — CTC/USDT P26_144

**Symbol:** CTC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.6034 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.9726 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -3.7110 |
| sortino_ratio | -1.2594 |
| max_drawdown | 0.8041 |
| cagr | -0.4551 |
| net_avg_win | 42.6653 |
| net_avg_loss | -64.8906 |
| avg_hold_time_bars | 16.6021 |
| exposure | 0.4400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
