# EMA Hourly Continuation — BOSON/USDT P12_200

**Symbol:** BOSON/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.7230 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.9113 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -2.3548 |
| sortino_ratio | -0.7041 |
| max_drawdown | 0.5642 |
| cagr | -0.2816 |
| net_avg_win | 69.7862 |
| net_avg_loss | -84.8633 |
| avg_hold_time_bars | 33.4324 |
| exposure | 0.6854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
