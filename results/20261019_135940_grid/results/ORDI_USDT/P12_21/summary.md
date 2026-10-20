# EMA Hourly Continuation — ORDI/USDT P12_21

**Symbol:** ORDI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1550 |
| net_profit_factor | 0.3886 |
| net_win_rate | 0.4084 |
| gross_profit_factor | 0.8629 |
| gross_win_rate | 0.4335 |
| sharpe_ratio | -12.5584 |
| sortino_ratio | -7.0147 |
| max_drawdown | 0.9999 |
| cagr | -0.9714 |
| net_avg_win | 10.0409 |
| net_avg_loss | -17.8348 |
| avg_hold_time_bars | 2.2858 |
| exposure | 0.1610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
