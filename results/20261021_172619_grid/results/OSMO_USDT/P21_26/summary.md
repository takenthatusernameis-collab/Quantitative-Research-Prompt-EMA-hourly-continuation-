# EMA Hourly Continuation — OSMO/USDT P21_26

**Symbol:** OSMO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.5071 |
| net_win_rate | 0.4108 |
| gross_profit_factor | 0.8012 |
| gross_win_rate | 0.4108 |
| sharpe_ratio | -4.2932 |
| sortino_ratio | -1.0607 |
| max_drawdown | 0.7227 |
| cagr | -0.3892 |
| net_avg_win | 59.8725 |
| net_avg_loss | -82.3162 |
| avg_hold_time_bars | 5.0606 |
| exposure | 0.0683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
