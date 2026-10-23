# EMA Hourly Continuation — BICO/USDT P21_34

**Symbol:** BICO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1049 |
| net_profit_factor | 0.3619 |
| net_win_rate | 0.4194 |
| gross_profit_factor | 0.7975 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -8.9320 |
| sortino_ratio | -4.1166 |
| max_drawdown | 0.9931 |
| cagr | -0.8621 |
| net_avg_win | 12.8001 |
| net_avg_loss | -25.5550 |
| avg_hold_time_bars | 3.2850 |
| exposure | 0.1566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
