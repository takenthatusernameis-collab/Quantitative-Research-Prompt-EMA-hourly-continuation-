# EMA Hourly Continuation — CVX/USDT P26_144

**Symbol:** CVX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.7972 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9625 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -1.3081 |
| sortino_ratio | -0.3701 |
| max_drawdown | 0.3568 |
| cagr | -0.1580 |
| net_avg_win | 71.0676 |
| net_avg_loss | -87.3407 |
| avg_hold_time_bars | 24.3367 |
| exposure | 0.4336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
