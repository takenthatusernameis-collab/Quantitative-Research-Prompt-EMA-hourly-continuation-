# EMA Hourly Continuation — PEPE/USDT P12_34

**Symbol:** PEPE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7219 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9155 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -2.3519 |
| sortino_ratio | -0.7566 |
| max_drawdown | 0.5890 |
| cagr | -0.2930 |
| net_avg_win | 62.1172 |
| net_avg_loss | -78.8987 |
| avg_hold_time_bars | 6.9272 |
| exposure | 0.1600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
