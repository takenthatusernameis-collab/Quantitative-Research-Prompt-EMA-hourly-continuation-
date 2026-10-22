# EMA Hourly Continuation — LUNC/USDT P20_89

**Symbol:** LUNC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 811 |
| net_profit_factor | 0.4319 |
| net_win_rate | 0.4402 |
| gross_profit_factor | 0.7590 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -6.5198 |
| sortino_ratio | -2.6206 |
| max_drawdown | 0.9605 |
| cagr | -0.7168 |
| net_avg_win | 20.3976 |
| net_avg_loss | -37.1391 |
| avg_hold_time_bars | 9.6227 |
| exposure | 0.3547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
