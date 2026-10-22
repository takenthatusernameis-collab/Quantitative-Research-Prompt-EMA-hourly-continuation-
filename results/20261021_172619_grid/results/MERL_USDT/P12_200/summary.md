# EMA Hourly Continuation — MERL/USDT P12_200

**Symbol:** MERL/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.7924 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.9028 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -1.1916 |
| sortino_ratio | -0.2776 |
| max_drawdown | 0.3166 |
| cagr | -0.1212 |
| net_avg_win | 83.1234 |
| net_avg_loss | -94.4802 |
| avg_hold_time_bars | 62.8433 |
| exposure | 0.7677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
