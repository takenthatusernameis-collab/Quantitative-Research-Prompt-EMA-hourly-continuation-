# EMA Hourly Continuation — EUL/USDT P20_55

**Symbol:** EUL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.6264 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.8130 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -2.8089 |
| sortino_ratio | -0.8955 |
| max_drawdown | 0.6624 |
| cagr | -0.3371 |
| net_avg_win | 46.3250 |
| net_avg_loss | -64.2985 |
| avg_hold_time_bars | 9.8363 |
| exposure | 0.2240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
