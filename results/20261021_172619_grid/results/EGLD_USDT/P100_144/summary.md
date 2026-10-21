# EMA Hourly Continuation — EGLD/USDT P100_144

**Symbol:** EGLD/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.6193 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.8798 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -2.1087 |
| sortino_ratio | -0.4656 |
| max_drawdown | 0.4177 |
| cagr | -0.1913 |
| net_avg_win | 59.4858 |
| net_avg_loss | -86.8390 |
| avg_hold_time_bars | 6.0630 |
| exposure | 0.0656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
