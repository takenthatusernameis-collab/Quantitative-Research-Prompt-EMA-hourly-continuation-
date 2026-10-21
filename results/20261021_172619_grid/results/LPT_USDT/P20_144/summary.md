# EMA Hourly Continuation — LPT/USDT P20_144

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.7627 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9239 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -1.7659 |
| sortino_ratio | -0.5084 |
| max_drawdown | 0.4555 |
| cagr | -0.2091 |
| net_avg_win | 73.0203 |
| net_avg_loss | -88.0951 |
| avg_hold_time_bars | 27.3276 |
| exposure | 0.5080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
