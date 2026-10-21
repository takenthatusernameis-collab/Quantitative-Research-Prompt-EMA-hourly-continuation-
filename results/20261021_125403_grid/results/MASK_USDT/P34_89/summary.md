# EMA Hourly Continuation — MASK/USDT P34_89

**Symbol:** MASK/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.5673 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8270 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -3.3854 |
| sortino_ratio | -1.0640 |
| max_drawdown | 0.7204 |
| cagr | -0.3887 |
| net_avg_win | 40.9759 |
| net_avg_loss | -63.0639 |
| avg_hold_time_bars | 10.1027 |
| exposure | 0.2236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
