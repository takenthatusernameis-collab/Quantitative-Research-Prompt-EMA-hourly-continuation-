# EMA Hourly Continuation — TRB/USDT P21_50

**Symbol:** TRB/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.3682 |
| net_win_rate | 0.3948 |
| gross_profit_factor | 0.6620 |
| gross_win_rate | 0.4227 |
| sharpe_ratio | -10.0239 |
| sortino_ratio | -4.6389 |
| max_drawdown | 0.9970 |
| cagr | -0.9003 |
| net_avg_win | 13.7010 |
| net_avg_loss | -24.2761 |
| avg_hold_time_bars | 4.3510 |
| exposure | 0.2115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
