# EMA Hourly Continuation — AKT/USDT P55_144

**Symbol:** AKT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.9835 |
| net_win_rate | 0.5460 |
| gross_profit_factor | 1.1899 |
| gross_win_rate | 0.5460 |
| sharpe_ratio | -0.0370 |
| sortino_ratio | -0.0097 |
| max_drawdown | 0.1531 |
| cagr | -0.0107 |
| net_avg_win | 89.1033 |
| net_avg_loss | -108.9589 |
| avg_hold_time_bars | 15.8558 |
| exposure | 0.2350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
