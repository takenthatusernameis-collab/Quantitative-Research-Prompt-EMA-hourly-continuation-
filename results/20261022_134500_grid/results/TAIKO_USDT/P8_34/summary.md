# EMA Hourly Continuation — TAIKO/USDT P8_34

**Symbol:** TAIKO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1241 |
| net_profit_factor | 0.5883 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.9620 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -8.0295 |
| sortino_ratio | -4.0681 |
| max_drawdown | 0.9918 |
| cagr | -0.8658 |
| net_avg_win | 24.9454 |
| net_avg_loss | -35.7867 |
| avg_hold_time_bars | 6.1741 |
| exposure | 0.3680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
