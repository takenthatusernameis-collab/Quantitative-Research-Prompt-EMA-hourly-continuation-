# EMA Hourly Continuation — CSPR/USDT P8_200

**Symbol:** CSPR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.6890 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.8317 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -2.4282 |
| sortino_ratio | -0.7035 |
| max_drawdown | 0.5752 |
| cagr | -0.2769 |
| net_avg_win | 65.3017 |
| net_avg_loss | -78.2200 |
| avg_hold_time_bars | 37.8062 |
| exposure | 0.7183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
