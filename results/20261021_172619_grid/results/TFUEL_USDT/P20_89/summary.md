# EMA Hourly Continuation — TFUEL/USDT P20_89

**Symbol:** TFUEL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 587 |
| net_profit_factor | 0.5960 |
| net_win_rate | 0.4242 |
| gross_profit_factor | 0.7742 |
| gross_win_rate | 0.4242 |
| sharpe_ratio | -4.3818 |
| sortino_ratio | -1.5002 |
| max_drawdown | 0.8294 |
| cagr | -0.4987 |
| net_avg_win | 48.8771 |
| net_avg_loss | -60.4116 |
| avg_hold_time_bars | 12.9267 |
| exposure | 0.3434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
