# EMA Hourly Continuation — DEGEN/USDT P8_20

**Symbol:** DEGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.7879 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 1.0031 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -2.0432 |
| sortino_ratio | -0.6890 |
| max_drawdown | 0.6063 |
| cagr | -0.2724 |
| net_avg_win | 74.2188 |
| net_avg_loss | -92.8487 |
| avg_hold_time_bars | 6.2058 |
| exposure | 0.1565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
