# EMA Hourly Continuation — CFX/USDT P55_144

**Symbol:** CFX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.6199 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9194 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -2.9861 |
| sortino_ratio | -0.8836 |
| max_drawdown | 0.6657 |
| cagr | -0.3459 |
| net_avg_win | 49.7425 |
| net_avg_loss | -75.3330 |
| avg_hold_time_bars | 13.6734 |
| exposure | 0.2760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
