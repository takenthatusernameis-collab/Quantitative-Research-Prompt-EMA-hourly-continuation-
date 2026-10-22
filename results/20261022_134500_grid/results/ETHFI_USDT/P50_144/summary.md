# EMA Hourly Continuation — ETHFI/USDT P50_144

**Symbol:** ETHFI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.7188 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 0.9980 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -2.3855 |
| sortino_ratio | -0.7505 |
| max_drawdown | 0.5973 |
| cagr | -0.2969 |
| net_avg_win | 61.7568 |
| net_avg_loss | -83.8472 |
| avg_hold_time_bars | 13.1382 |
| exposure | 0.2938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
