# EMA Hourly Continuation — GRAM/USDT P20_21

**Symbol:** GRAM/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 91 |
| net_profit_factor | 0.7136 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0552 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -0.9624 |
| sortino_ratio | -0.1322 |
| max_drawdown | 0.1569 |
| cagr | -0.0590 |
| net_avg_win | 75.1183 |
| net_avg_loss | -112.4460 |
| avg_hold_time_bars | 4.9780 |
| exposure | 0.0206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
