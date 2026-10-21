# EMA Hourly Continuation — SAFE/USDT P26_55

**Symbol:** SAFE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.8048 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0787 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -1.5063 |
| sortino_ratio | -0.4670 |
| max_drawdown | 0.4770 |
| cagr | -0.1929 |
| net_avg_win | 71.6877 |
| net_avg_loss | -95.4995 |
| avg_hold_time_bars | 7.9478 |
| exposure | 0.1674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
