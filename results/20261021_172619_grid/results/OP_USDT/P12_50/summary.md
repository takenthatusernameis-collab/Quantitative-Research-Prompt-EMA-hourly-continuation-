# EMA Hourly Continuation — OP/USDT P12_50

**Symbol:** OP/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.7165 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9111 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -2.6217 |
| sortino_ratio | -0.9198 |
| max_drawdown | 0.6775 |
| cagr | -0.3445 |
| net_avg_win | 57.3572 |
| net_avg_loss | -72.7332 |
| avg_hold_time_bars | 11.3884 |
| exposure | 0.3132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
