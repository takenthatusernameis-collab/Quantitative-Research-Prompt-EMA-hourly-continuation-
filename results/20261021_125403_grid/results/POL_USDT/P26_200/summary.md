# EMA Hourly Continuation — POL/USDT P26_200

**Symbol:** POL/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.9932 |
| net_win_rate | 0.5441 |
| gross_profit_factor | 1.1899 |
| gross_win_rate | 0.5441 |
| sharpe_ratio | 0.0181 |
| sortino_ratio | 0.0042 |
| max_drawdown | 0.2104 |
| cagr | -0.0034 |
| net_avg_win | 86.0986 |
| net_avg_loss | -103.4467 |
| avg_hold_time_bars | 52.7203 |
| exposure | 0.6255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
