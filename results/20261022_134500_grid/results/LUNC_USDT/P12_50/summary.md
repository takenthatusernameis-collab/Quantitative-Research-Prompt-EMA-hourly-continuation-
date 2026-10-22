# EMA Hourly Continuation — LUNC/USDT P12_50

**Symbol:** LUNC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1160 |
| net_profit_factor | 0.4052 |
| net_win_rate | 0.4103 |
| gross_profit_factor | 0.7797 |
| gross_win_rate | 0.4284 |
| sharpe_ratio | -9.5474 |
| sortino_ratio | -4.6010 |
| max_drawdown | 0.9965 |
| cagr | -0.8941 |
| net_avg_win | 14.2618 |
| net_avg_loss | -24.4928 |
| avg_hold_time_bars | 6.1440 |
| exposure | 0.3240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
