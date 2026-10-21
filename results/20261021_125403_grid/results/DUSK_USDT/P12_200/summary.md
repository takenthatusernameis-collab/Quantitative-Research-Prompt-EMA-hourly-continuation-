# EMA Hourly Continuation — DUSK/USDT P12_200

**Symbol:** DUSK/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.9061 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0256 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -0.4555 |
| sortino_ratio | -0.1077 |
| max_drawdown | 0.2005 |
| cagr | -0.0514 |
| net_avg_win | 86.7638 |
| net_avg_loss | -98.6169 |
| avg_hold_time_bars | 60.7978 |
| exposure | 0.7517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
