# EMA Hourly Continuation — AKT/USDT P100_144

**Symbol:** AKT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 1.1161 |
| net_win_rate | 0.5991 |
| gross_profit_factor | 1.4548 |
| gross_win_rate | 0.5991 |
| sharpe_ratio | 0.6316 |
| sortino_ratio | 0.1389 |
| max_drawdown | 0.1734 |
| cagr | 0.0563 |
| net_avg_win | 106.5324 |
| net_avg_loss | -142.6430 |
| avg_hold_time_bars | 6.3739 |
| exposure | 0.0643 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
