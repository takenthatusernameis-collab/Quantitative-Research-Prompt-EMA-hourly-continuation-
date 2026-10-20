# EMA Hourly Continuation — STRAX/USDT P50_89

**Symbol:** STRAX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.4479 |
| net_win_rate | 0.3920 |
| gross_profit_factor | 0.8040 |
| gross_win_rate | 0.4182 |
| sharpe_ratio | -8.5178 |
| sortino_ratio | -3.2653 |
| max_drawdown | 0.9831 |
| cagr | -0.8047 |
| net_avg_win | 27.9793 |
| net_avg_loss | -40.2822 |
| avg_hold_time_bars | 5.6327 |
| exposure | 0.1872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
