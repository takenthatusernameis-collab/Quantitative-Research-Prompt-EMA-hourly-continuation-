# EMA Hourly Continuation — FET/USDT P8_144

**Symbol:** FET/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.9911 |
| net_win_rate | 0.5322 |
| gross_profit_factor | 1.1213 |
| gross_win_rate | 0.5322 |
| sharpe_ratio | 0.0022 |
| sortino_ratio | 0.0006 |
| max_drawdown | 0.2037 |
| cagr | -0.0065 |
| net_avg_win | 99.9890 |
| net_avg_loss | -114.7548 |
| avg_hold_time_bars | 47.7544 |
| exposure | 0.7424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
