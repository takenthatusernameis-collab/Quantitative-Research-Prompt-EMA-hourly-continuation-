# EMA Hourly Continuation — EUL/USDT P8_21

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1480 |
| net_profit_factor | 0.3236 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.6189 |
| gross_win_rate | 0.4209 |
| sharpe_ratio | -11.5857 |
| sortino_ratio | -6.2920 |
| max_drawdown | 0.9996 |
| cagr | -0.9567 |
| net_avg_win | 8.0779 |
| net_avg_loss | -16.6423 |
| avg_hold_time_bars | 4.1439 |
| exposure | 0.2788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
