# EMA Hourly Continuation — ADA/USDT P89_144

**Symbol:** ADA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.4593 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.9004 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -5.0006 |
| sortino_ratio | -1.5314 |
| max_drawdown | 0.8514 |
| cagr | -0.5302 |
| net_avg_win | 33.4320 |
| net_avg_loss | -60.9365 |
| avg_hold_time_bars | 4.9262 |
| exposure | 0.1061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
