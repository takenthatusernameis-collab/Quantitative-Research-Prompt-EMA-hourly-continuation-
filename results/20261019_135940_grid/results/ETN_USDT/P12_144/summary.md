# EMA Hourly Continuation — ETN/USDT P12_144

**Symbol:** ETN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.4684 |
| net_win_rate | 0.3907 |
| gross_profit_factor | 0.6632 |
| gross_win_rate | 0.3990 |
| sharpe_ratio | -6.7206 |
| sortino_ratio | -2.5134 |
| max_drawdown | 0.9278 |
| cagr | -0.7060 |
| net_avg_win | 34.7818 |
| net_avg_loss | -47.6049 |
| avg_hold_time_bars | 16.7997 |
| exposure | 0.5466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
