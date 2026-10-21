# EMA Hourly Continuation — DGB/USDT P12_100

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.8552 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0546 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -1.1402 |
| sortino_ratio | -0.3730 |
| max_drawdown | 0.3787 |
| cagr | -0.1603 |
| net_avg_win | 78.8382 |
| net_avg_loss | -96.9280 |
| avg_hold_time_bars | 22.6898 |
| exposure | 0.5353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
