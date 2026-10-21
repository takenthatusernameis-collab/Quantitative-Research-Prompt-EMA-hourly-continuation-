# EMA Hourly Continuation — XEC/USDT P50_89

**Symbol:** XEC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.5699 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8406 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -3.6568 |
| sortino_ratio | -1.1193 |
| max_drawdown | 0.7323 |
| cagr | -0.4011 |
| net_avg_win | 45.5651 |
| net_avg_loss | -68.0278 |
| avg_hold_time_bars | 7.0763 |
| exposure | 0.1470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
