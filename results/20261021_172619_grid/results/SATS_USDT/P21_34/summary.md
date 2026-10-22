# EMA Hourly Continuation — SATS/USDT P21_34

**Symbol:** SATS/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.6546 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.9175 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -2.7545 |
| sortino_ratio | -0.7342 |
| max_drawdown | 0.6057 |
| cagr | -0.2901 |
| net_avg_win | 66.4696 |
| net_avg_loss | -88.6425 |
| avg_hold_time_bars | 5.1780 |
| exposure | 0.0829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
