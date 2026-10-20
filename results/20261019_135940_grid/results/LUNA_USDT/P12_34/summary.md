# EMA Hourly Continuation — LUNA/USDT P12_34

**Symbol:** LUNA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1435 |
| net_profit_factor | 0.4045 |
| net_win_rate | 0.4111 |
| gross_profit_factor | 0.8191 |
| gross_win_rate | 0.4321 |
| sharpe_ratio | -11.8178 |
| sortino_ratio | -6.3434 |
| max_drawdown | 0.9997 |
| cagr | -0.9591 |
| net_avg_win | 11.5098 |
| net_avg_loss | -19.8669 |
| avg_hold_time_bars | 3.5359 |
| exposure | 0.2306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
