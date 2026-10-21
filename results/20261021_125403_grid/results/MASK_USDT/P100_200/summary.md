# EMA Hourly Continuation — MASK/USDT P100_200

**Symbol:** MASK/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.6318 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9062 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -2.3744 |
| sortino_ratio | -0.5825 |
| max_drawdown | 0.5199 |
| cagr | -0.2353 |
| net_avg_win | 59.6465 |
| net_avg_loss | -86.4437 |
| avg_hold_time_bars | 13.1220 |
| exposure | 0.1760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
