# EMA Hourly Continuation — OGN/USDT P20_144

**Symbol:** OGN/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.5799 |
| net_win_rate | 0.4333 |
| gross_profit_factor | 0.8823 |
| gross_win_rate | 0.4456 |
| sharpe_ratio | -4.4621 |
| sortino_ratio | -1.3678 |
| max_drawdown | 0.8257 |
| cagr | -0.4878 |
| net_avg_win | 53.3142 |
| net_avg_loss | -70.2896 |
| avg_hold_time_bars | 26.0226 |
| exposure | 0.5735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
