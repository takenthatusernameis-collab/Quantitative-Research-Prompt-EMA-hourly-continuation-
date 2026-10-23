# EMA Hourly Continuation — CARV/USDT P12_20

**Symbol:** CARV/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1072 |
| net_profit_factor | 0.4103 |
| net_win_rate | 0.4272 |
| gross_profit_factor | 0.9122 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -11.3821 |
| sortino_ratio | -5.8881 |
| max_drawdown | 0.9977 |
| cagr | -0.9495 |
| net_avg_win | 15.1578 |
| net_avg_loss | -27.5551 |
| avg_hold_time_bars | 3.1409 |
| exposure | 0.1895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
