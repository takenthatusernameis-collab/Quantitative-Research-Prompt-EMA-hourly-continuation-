# EMA Hourly Continuation — ACE/USDT P34_144

**Symbol:** ACE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.8258 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0118 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.1292 |
| sortino_ratio | -0.2933 |
| max_drawdown | 0.4118 |
| cagr | -0.1283 |
| net_avg_win | 83.5644 |
| net_avg_loss | -101.1938 |
| avg_hold_time_bars | 27.5452 |
| exposure | 0.4138 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
