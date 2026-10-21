# EMA Hourly Continuation — MINA/USDT P20_144

**Symbol:** MINA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.9466 |
| net_win_rate | 0.5409 |
| gross_profit_factor | 1.1600 |
| gross_win_rate | 0.5409 |
| sharpe_ratio | -0.2731 |
| sortino_ratio | -0.0768 |
| max_drawdown | 0.2628 |
| cagr | -0.0403 |
| net_avg_win | 84.9902 |
| net_avg_loss | -105.7773 |
| avg_hold_time_bars | 34.1873 |
| exposure | 0.5890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
