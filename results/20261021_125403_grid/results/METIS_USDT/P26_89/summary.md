# EMA Hourly Continuation — METIS/USDT P26_89

**Symbol:** METIS/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.7795 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 0.9829 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -1.8146 |
| sortino_ratio | -0.5577 |
| max_drawdown | 0.5091 |
| cagr | -0.2263 |
| net_avg_win | 73.9613 |
| net_avg_loss | -91.6589 |
| avg_hold_time_bars | 13.7944 |
| exposure | 0.2897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
