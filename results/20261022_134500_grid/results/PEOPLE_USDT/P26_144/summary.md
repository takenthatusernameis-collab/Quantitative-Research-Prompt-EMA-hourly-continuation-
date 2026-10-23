# EMA Hourly Continuation — PEOPLE/USDT P26_144

**Symbol:** PEOPLE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.7716 |
| net_win_rate | 0.5049 |
| gross_profit_factor | 1.0132 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -1.5494 |
| sortino_ratio | -0.4448 |
| max_drawdown | 0.4430 |
| cagr | -0.1876 |
| net_avg_win | 66.9069 |
| net_avg_loss | -88.4271 |
| avg_hold_time_bars | 28.2990 |
| exposure | 0.5225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
