# EMA Hourly Continuation — SOL/USDT P12_144

**Symbol:** SOL/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.9281 |
| net_win_rate | 0.5367 |
| gross_profit_factor | 1.1455 |
| gross_win_rate | 0.5367 |
| sharpe_ratio | -0.3808 |
| sortino_ratio | -0.1015 |
| max_drawdown | 0.2192 |
| cagr | -0.0500 |
| net_avg_win | 85.2645 |
| net_avg_loss | -106.4075 |
| avg_hold_time_bars | 42.4516 |
| exposure | 0.6580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
