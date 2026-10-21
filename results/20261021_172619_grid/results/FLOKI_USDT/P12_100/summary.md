# EMA Hourly Continuation — FLOKI/USDT P12_100

**Symbol:** FLOKI/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.8295 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0010 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -1.1796 |
| sortino_ratio | -0.3618 |
| max_drawdown | 0.3709 |
| cagr | -0.1554 |
| net_avg_win | 72.7786 |
| net_avg_loss | -89.2851 |
| avg_hold_time_bars | 28.0175 |
| exposure | 0.5833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
