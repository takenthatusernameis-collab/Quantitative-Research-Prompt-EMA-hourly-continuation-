# EMA Hourly Continuation — ANKR/USDT P12_144

**Symbol:** ANKR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.8553 |
| net_win_rate | 0.5157 |
| gross_profit_factor | 1.0638 |
| gross_win_rate | 0.5157 |
| sharpe_ratio | -0.9275 |
| sortino_ratio | -0.2371 |
| max_drawdown | 0.3423 |
| cagr | -0.1056 |
| net_avg_win | 88.0956 |
| net_avg_loss | -109.6887 |
| avg_hold_time_bars | 50.9748 |
| exposure | 0.7368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
