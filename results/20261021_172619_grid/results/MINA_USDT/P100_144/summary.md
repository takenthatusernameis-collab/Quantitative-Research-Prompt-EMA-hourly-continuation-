# EMA Hourly Continuation — MINA/USDT P100_144

**Symbol:** MINA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.6977 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9850 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.8687 |
| sortino_ratio | -0.4565 |
| max_drawdown | 0.4303 |
| cagr | -0.1899 |
| net_avg_win | 65.3678 |
| net_avg_loss | -93.6963 |
| avg_hold_time_bars | 6.2345 |
| exposure | 0.0822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
