# EMA Hourly Continuation — ETHFI/USDT P55_89

**Symbol:** ETHFI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.4879 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.8245 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -6.1070 |
| sortino_ratio | -2.3059 |
| max_drawdown | 0.9415 |
| cagr | -0.6766 |
| net_avg_win | 28.4696 |
| net_avg_loss | -45.7226 |
| avg_hold_time_bars | 3.6151 |
| exposure | 0.1178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
