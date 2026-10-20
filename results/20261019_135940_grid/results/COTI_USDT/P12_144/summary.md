# EMA Hourly Continuation — COTI/USDT P12_144

**Symbol:** COTI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.7158 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9842 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -2.5742 |
| sortino_ratio | -0.8519 |
| max_drawdown | 0.6643 |
| cagr | -0.3365 |
| net_avg_win | 59.5455 |
| net_avg_loss | -79.6746 |
| avg_hold_time_bars | 26.2608 |
| exposure | 0.6637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
