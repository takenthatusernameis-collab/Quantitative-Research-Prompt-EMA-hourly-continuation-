# EMA Hourly Continuation — AVAX/USDT P50_144

**Symbol:** AVAX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.5437 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8799 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -4.3675 |
| sortino_ratio | -1.2885 |
| max_drawdown | 0.7955 |
| cagr | -0.4658 |
| net_avg_win | 47.7127 |
| net_avg_loss | -71.8030 |
| avg_hold_time_bars | 14.5159 |
| exposure | 0.2903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
