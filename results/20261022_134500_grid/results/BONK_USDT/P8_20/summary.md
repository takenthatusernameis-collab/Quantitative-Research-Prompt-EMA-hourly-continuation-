# EMA Hourly Continuation — BONK/USDT P8_20

**Symbol:** BONK/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1692 |
| net_profit_factor | 0.5120 |
| net_win_rate | 0.4220 |
| gross_profit_factor | 0.9142 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -11.6536 |
| sortino_ratio | -6.7215 |
| max_drawdown | 0.9998 |
| cagr | -0.9672 |
| net_avg_win | 14.6933 |
| net_avg_loss | -20.9500 |
| avg_hold_time_bars | 2.6365 |
| exposure | 0.2028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
