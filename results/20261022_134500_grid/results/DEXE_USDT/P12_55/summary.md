# EMA Hourly Continuation — DEXE/USDT P12_55

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 985 |
| net_profit_factor | 0.4466 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.7850 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -6.9746 |
| sortino_ratio | -3.0718 |
| max_drawdown | 0.9776 |
| cagr | -0.7791 |
| net_avg_win | 18.1366 |
| net_avg_loss | -32.1160 |
| avg_hold_time_bars | 10.4132 |
| exposure | 0.4662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
