# EMA Hourly Continuation — DIA/USDT P12_200

**Symbol:** DIA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 1.1315 |
| net_win_rate | 0.5734 |
| gross_profit_factor | 1.3386 |
| gross_win_rate | 0.5734 |
| sharpe_ratio | 0.6678 |
| sortino_ratio | 0.1649 |
| max_drawdown | 0.1284 |
| cagr | 0.0674 |
| net_avg_win | 93.8099 |
| net_avg_loss | -111.4477 |
| avg_hold_time_bars | 57.7657 |
| exposure | 0.7476 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
