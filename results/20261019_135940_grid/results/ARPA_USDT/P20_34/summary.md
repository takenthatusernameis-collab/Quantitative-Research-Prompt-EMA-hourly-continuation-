# EMA Hourly Continuation — ARPA/USDT P20_34

**Symbol:** ARPA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1176 |
| net_profit_factor | 0.3602 |
| net_win_rate | 0.3912 |
| gross_profit_factor | 0.8032 |
| gross_win_rate | 0.4235 |
| sharpe_ratio | -11.5517 |
| sortino_ratio | -5.6602 |
| max_drawdown | 0.9992 |
| cagr | -0.9404 |
| net_avg_win | 12.2270 |
| net_avg_loss | -21.8105 |
| avg_hold_time_bars | 3.5187 |
| exposure | 0.1872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
