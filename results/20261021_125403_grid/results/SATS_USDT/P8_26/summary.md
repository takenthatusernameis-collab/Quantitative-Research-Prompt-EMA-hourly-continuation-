# EMA Hourly Continuation — SATS/USDT P8_26

**Symbol:** SATS/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.8196 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0794 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -1.7861 |
| sortino_ratio | -0.6885 |
| max_drawdown | 0.5940 |
| cagr | -0.2738 |
| net_avg_win | 67.1271 |
| net_avg_loss | -87.7472 |
| avg_hold_time_bars | 6.6814 |
| exposure | 0.2192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
