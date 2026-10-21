# EMA Hourly Continuation — IOTA/USDT P12_200

**Symbol:** IOTA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.9037 |
| net_win_rate | 0.5197 |
| gross_profit_factor | 1.0767 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -0.5020 |
| sortino_ratio | -0.1258 |
| max_drawdown | 0.2144 |
| cagr | -0.0595 |
| net_avg_win | 84.8377 |
| net_avg_loss | -101.5951 |
| avg_hold_time_bars | 54.2500 |
| exposure | 0.7496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
