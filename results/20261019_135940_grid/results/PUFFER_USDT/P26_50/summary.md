# EMA Hourly Continuation — PUFFER/USDT P26_50

**Symbol:** PUFFER/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.5796 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9739 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -5.1680 |
| sortino_ratio | -2.1791 |
| max_drawdown | 0.8810 |
| cagr | -0.6488 |
| net_avg_win | 35.1195 |
| net_avg_loss | -56.4998 |
| avg_hold_time_bars | 4.3483 |
| exposure | 0.1759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
