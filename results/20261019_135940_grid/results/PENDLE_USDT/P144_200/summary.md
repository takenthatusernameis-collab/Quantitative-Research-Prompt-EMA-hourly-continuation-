# EMA Hourly Continuation — PENDLE/USDT P144_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.4797 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.7818 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -4.1693 |
| sortino_ratio | -1.2827 |
| max_drawdown | 0.7778 |
| cagr | -0.4506 |
| net_avg_win | 33.5154 |
| net_avg_loss | -59.3260 |
| avg_hold_time_bars | 4.1738 |
| exposure | 0.0884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
