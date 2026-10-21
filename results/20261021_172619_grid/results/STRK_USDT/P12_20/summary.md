# EMA Hourly Continuation — STRK/USDT P12_20

**Symbol:** STRK/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.7683 |
| net_win_rate | 0.5081 |
| gross_profit_factor | 1.0231 |
| gross_win_rate | 0.5081 |
| sharpe_ratio | -1.2651 |
| sortino_ratio | -0.2864 |
| max_drawdown | 0.3160 |
| cagr | -0.1234 |
| net_avg_win | 74.1045 |
| net_avg_loss | -99.6210 |
| avg_hold_time_bars | 4.6855 |
| exposure | 0.0528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
