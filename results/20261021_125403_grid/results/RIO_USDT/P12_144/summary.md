# EMA Hourly Continuation — RIO/USDT P12_144

**Symbol:** RIO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.9226 |
| net_win_rate | 0.5069 |
| gross_profit_factor | 1.0256 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -0.4926 |
| sortino_ratio | -0.1478 |
| max_drawdown | 0.2665 |
| cagr | -0.0713 |
| net_avg_win | 91.0890 |
| net_avg_loss | -101.4959 |
| avg_hold_time_bars | 30.1820 |
| exposure | 0.6014 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
