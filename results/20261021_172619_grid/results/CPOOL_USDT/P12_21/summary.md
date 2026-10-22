# EMA Hourly Continuation — CPOOL/USDT P12_21

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.8145 |
| net_win_rate | 0.5049 |
| gross_profit_factor | 1.0392 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -1.2618 |
| sortino_ratio | -0.3159 |
| max_drawdown | 0.3900 |
| cagr | -0.1367 |
| net_avg_win | 87.9862 |
| net_avg_loss | -110.1729 |
| avg_hold_time_bars | 5.3279 |
| exposure | 0.0739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
