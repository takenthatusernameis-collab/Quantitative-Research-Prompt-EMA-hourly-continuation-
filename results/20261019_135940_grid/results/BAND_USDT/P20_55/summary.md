# EMA Hourly Continuation — BAND/USDT P20_55

**Symbol:** BAND/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 883 |
| net_profit_factor | 0.5732 |
| net_win_rate | 0.4564 |
| gross_profit_factor | 0.9739 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -6.2228 |
| sortino_ratio | -2.5914 |
| max_drawdown | 0.9594 |
| cagr | -0.7178 |
| net_avg_win | 31.9518 |
| net_avg_loss | -46.8030 |
| avg_hold_time_bars | 6.8007 |
| exposure | 0.2717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
