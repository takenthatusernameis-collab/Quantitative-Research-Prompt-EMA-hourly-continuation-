# EMA Hourly Continuation — MASK/USDT P50_144

**Symbol:** MASK/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.5037 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.8645 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -4.7977 |
| sortino_ratio | -1.5588 |
| max_drawdown | 0.8621 |
| cagr | -0.5396 |
| net_avg_win | 34.8147 |
| net_avg_loss | -59.3749 |
| avg_hold_time_bars | 10.9445 |
| exposure | 0.2691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
