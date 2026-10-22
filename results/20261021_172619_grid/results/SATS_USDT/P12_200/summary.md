# EMA Hourly Continuation — SATS/USDT P12_200

**Symbol:** SATS/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.7442 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.8773 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -1.4735 |
| sortino_ratio | -0.3693 |
| max_drawdown | 0.3916 |
| cagr | -0.1569 |
| net_avg_win | 68.7576 |
| net_avg_loss | -83.3798 |
| avg_hold_time_bars | 49.8910 |
| exposure | 0.7044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
