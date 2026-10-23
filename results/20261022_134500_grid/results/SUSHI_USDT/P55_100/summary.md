# EMA Hourly Continuation — SUSHI/USDT P55_100

**Symbol:** SUSHI/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.5495 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.9236 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -5.4936 |
| sortino_ratio | -1.9830 |
| max_drawdown | 0.9136 |
| cagr | -0.6188 |
| net_avg_win | 37.7236 |
| net_avg_loss | -56.0962 |
| avg_hold_time_bars | 4.9573 |
| exposure | 0.1472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
