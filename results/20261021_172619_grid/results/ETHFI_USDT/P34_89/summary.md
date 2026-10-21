# EMA Hourly Continuation — ETHFI/USDT P34_89

**Symbol:** ETHFI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.8229 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 1.0041 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -1.4435 |
| sortino_ratio | -0.4303 |
| max_drawdown | 0.4678 |
| cagr | -0.1808 |
| net_avg_win | 85.1774 |
| net_avg_loss | -101.6123 |
| avg_hold_time_bars | 11.3940 |
| exposure | 0.2248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
