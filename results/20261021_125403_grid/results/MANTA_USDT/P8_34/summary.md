# EMA Hourly Continuation — MANTA/USDT P8_34

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.8086 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0437 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -2.0249 |
| sortino_ratio | -0.7941 |
| max_drawdown | 0.6066 |
| cagr | -0.3067 |
| net_avg_win | 66.8590 |
| net_avg_loss | -85.6160 |
| avg_hold_time_bars | 10.6627 |
| exposure | 0.3620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
