# EMA Hourly Continuation — ORCA/USDT P50_144

**Symbol:** ORCA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.5778 |
| net_win_rate | 0.4654 |
| gross_profit_factor | 0.8764 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -3.5426 |
| sortino_ratio | -1.0892 |
| max_drawdown | 0.7483 |
| cagr | -0.4044 |
| net_avg_win | 44.8666 |
| net_avg_loss | -67.6015 |
| avg_hold_time_bars | 13.2432 |
| exposure | 0.2871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
