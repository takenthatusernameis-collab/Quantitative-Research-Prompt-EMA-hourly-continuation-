# EMA Hourly Continuation — BDX/USDT P20_144

**Symbol:** BDX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.5059 |
| net_win_rate | 0.4248 |
| gross_profit_factor | 0.7850 |
| gross_win_rate | 0.4270 |
| sharpe_ratio | -4.8250 |
| sortino_ratio | -1.4631 |
| max_drawdown | 0.8309 |
| cagr | -0.4953 |
| net_avg_win | 43.7556 |
| net_avg_loss | -63.8681 |
| avg_hold_time_bars | 16.2456 |
| exposure | 0.3338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
