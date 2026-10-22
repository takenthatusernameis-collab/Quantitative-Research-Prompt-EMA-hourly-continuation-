# EMA Hourly Continuation — DBR/USDT P55_144

**Symbol:** DBR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.5140 |
| net_win_rate | 0.4432 |
| gross_profit_factor | 0.8687 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -4.5188 |
| sortino_ratio | -1.3311 |
| max_drawdown | 0.7345 |
| cagr | -0.4745 |
| net_avg_win | 49.1544 |
| net_avg_loss | -76.1187 |
| avg_hold_time_bars | 13.5028 |
| exposure | 0.2703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
