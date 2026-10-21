# EMA Hourly Continuation — SATS/USDT P12_89

**Symbol:** SATS/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.8089 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9775 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -1.5242 |
| sortino_ratio | -0.4878 |
| max_drawdown | 0.4835 |
| cagr | -0.2028 |
| net_avg_win | 74.0119 |
| net_avg_loss | -89.3459 |
| avg_hold_time_bars | 22.7679 |
| exposure | 0.5193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
