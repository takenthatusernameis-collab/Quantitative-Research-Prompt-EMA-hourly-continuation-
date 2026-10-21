# EMA Hourly Continuation — LINK/USDT P55_144

**Symbol:** LINK/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.8611 |
| net_win_rate | 0.5362 |
| gross_profit_factor | 1.1345 |
| gross_win_rate | 0.5362 |
| sharpe_ratio | -0.7701 |
| sortino_ratio | -0.1938 |
| max_drawdown | 0.2896 |
| cagr | -0.0866 |
| net_avg_win | 77.3476 |
| net_avg_loss | -103.8409 |
| avg_hold_time_bars | 16.1349 |
| exposure | 0.2230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
