# EMA Hourly Continuation — MERL/USDT P34_144

**Symbol:** MERL/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.7618 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.8901 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -1.6022 |
| sortino_ratio | -0.4231 |
| max_drawdown | 0.4369 |
| cagr | -0.1782 |
| net_avg_win | 76.2007 |
| net_avg_loss | -89.5826 |
| avg_hold_time_bars | 24.4783 |
| exposure | 0.3849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
