# EMA Hourly Continuation — DBR/USDT P12_144

**Symbol:** DBR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.6520 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.8325 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -2.4264 |
| sortino_ratio | -0.6628 |
| max_drawdown | 0.4723 |
| cagr | -0.2630 |
| net_avg_win | 62.6473 |
| net_avg_loss | -82.7839 |
| avg_hold_time_bars | 36.7534 |
| exposure | 0.6187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
