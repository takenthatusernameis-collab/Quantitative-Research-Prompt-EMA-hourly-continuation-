# EMA Hourly Continuation — AGLD/USDT P34_50

**Symbol:** AGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 901 |
| net_profit_factor | 0.3997 |
| net_win_rate | 0.4229 |
| gross_profit_factor | 0.8260 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -8.4082 |
| sortino_ratio | -3.5639 |
| max_drawdown | 0.9887 |
| cagr | -0.8278 |
| net_avg_win | 17.2724 |
| net_avg_loss | -31.6586 |
| avg_hold_time_bars | 3.5150 |
| exposure | 0.1433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
