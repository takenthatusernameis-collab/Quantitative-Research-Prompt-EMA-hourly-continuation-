# EMA Hourly Continuation — LUNA/USDT P100_200

**Symbol:** LUNA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.4656 |
| net_win_rate | 0.4354 |
| gross_profit_factor | 0.7676 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -4.8996 |
| sortino_ratio | -1.4887 |
| max_drawdown | 0.8344 |
| cagr | -0.5075 |
| net_avg_win | 36.3972 |
| net_avg_loss | -60.2897 |
| avg_hold_time_bars | 9.1116 |
| exposure | 0.1893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
