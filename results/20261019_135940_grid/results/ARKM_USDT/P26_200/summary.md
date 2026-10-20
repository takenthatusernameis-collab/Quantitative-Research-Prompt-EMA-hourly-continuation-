# EMA Hourly Continuation — ARKM/USDT P26_200

**Symbol:** ARKM/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.6752 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.9008 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -2.3954 |
| sortino_ratio | -0.6731 |
| max_drawdown | 0.5800 |
| cagr | -0.2746 |
| net_avg_win | 61.1841 |
| net_avg_loss | -79.6112 |
| avg_hold_time_bars | 30.7139 |
| exposure | 0.5612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
