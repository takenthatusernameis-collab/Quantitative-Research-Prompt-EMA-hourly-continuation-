# EMA Hourly Continuation — TRADE/USDT P26_34

**Symbol:** TRADE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 856 |
| net_profit_factor | 0.2814 |
| net_win_rate | 0.3493 |
| gross_profit_factor | 0.6466 |
| gross_win_rate | 0.3680 |
| sharpe_ratio | -11.6999 |
| sortino_ratio | -4.9215 |
| max_drawdown | 0.9987 |
| cagr | -0.9276 |
| net_avg_win | 13.0801 |
| net_avg_loss | -24.9501 |
| avg_hold_time_bars | 2.7979 |
| exposure | 0.1089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
