# EMA Hourly Continuation — AVAX/USDT P8_50

**Symbol:** AVAX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.7267 |
| net_win_rate | 0.4736 |
| gross_profit_factor | 0.9243 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -2.8251 |
| sortino_ratio | -1.0217 |
| max_drawdown | 0.7171 |
| cagr | -0.3747 |
| net_avg_win | 60.3627 |
| net_avg_loss | -74.7345 |
| avg_hold_time_bars | 14.2811 |
| exposure | 0.4180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
