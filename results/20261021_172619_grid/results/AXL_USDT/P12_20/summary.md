# EMA Hourly Continuation — AXL/USDT P12_20

**Symbol:** AXL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.5537 |
| net_win_rate | 0.4244 |
| gross_profit_factor | 0.7627 |
| gross_win_rate | 0.4244 |
| sharpe_ratio | -4.2468 |
| sortino_ratio | -1.2686 |
| max_drawdown | 0.7755 |
| cagr | -0.4448 |
| net_avg_win | 51.0408 |
| net_avg_loss | -67.9561 |
| avg_hold_time_bars | 4.5260 |
| exposure | 0.0907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
