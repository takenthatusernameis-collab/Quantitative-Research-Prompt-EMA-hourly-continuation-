# EMA Hourly Continuation — ALEX/USDT P8_144

**Symbol:** ALEX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6135 |
| net_win_rate | 0.4373 |
| gross_profit_factor | 0.8670 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -3.5067 |
| sortino_ratio | -0.9919 |
| max_drawdown | 0.7151 |
| cagr | -0.3763 |
| net_avg_win | 61.9177 |
| net_avg_loss | -78.4506 |
| avg_hold_time_bars | 41.3292 |
| exposure | 0.7646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
