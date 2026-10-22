# EMA Hourly Continuation — CHZ/USDT P20_34

**Symbol:** CHZ/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1188 |
| net_profit_factor | 0.4109 |
| net_win_rate | 0.4234 |
| gross_profit_factor | 0.9288 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -10.8644 |
| sortino_ratio | -5.3335 |
| max_drawdown | 0.9988 |
| cagr | -0.9317 |
| net_avg_win | 13.8511 |
| net_avg_loss | -24.7522 |
| avg_hold_time_bars | 2.6448 |
| exposure | 0.1428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
