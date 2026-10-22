# EMA Hourly Continuation — REZ/USDT P26_144

**Symbol:** REZ/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.9626 |
| net_win_rate | 0.5332 |
| gross_profit_factor | 1.1345 |
| gross_win_rate | 0.5332 |
| sharpe_ratio | -0.1955 |
| sortino_ratio | -0.0552 |
| max_drawdown | 0.2060 |
| cagr | -0.0314 |
| net_avg_win | 97.0592 |
| net_avg_loss | -115.1574 |
| avg_hold_time_bars | 27.6658 |
| exposure | 0.4812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
