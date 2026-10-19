# EMA Hourly Continuation — STRK/USDT P12_34

**Symbol:** STRK/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1275 |
| net_profit_factor | 0.5125 |
| net_win_rate | 0.4494 |
| gross_profit_factor | 0.9041 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -8.0149 |
| sortino_ratio | -4.0238 |
| max_drawdown | 0.9931 |
| cagr | -0.8599 |
| net_avg_win | 18.2169 |
| net_avg_loss | -29.0119 |
| avg_hold_time_bars | 3.9459 |
| exposure | 0.2287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
