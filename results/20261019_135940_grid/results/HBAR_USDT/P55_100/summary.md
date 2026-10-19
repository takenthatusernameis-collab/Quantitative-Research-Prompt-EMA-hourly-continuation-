# EMA Hourly Continuation — HBAR/USDT P55_100

**Symbol:** HBAR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.4454 |
| net_win_rate | 0.4353 |
| gross_profit_factor | 0.8329 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -6.5174 |
| sortino_ratio | -2.2888 |
| max_drawdown | 0.9458 |
| cagr | -0.6805 |
| net_avg_win | 28.1501 |
| net_avg_loss | -48.7186 |
| avg_hold_time_bars | 4.6861 |
| exposure | 0.1316 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
