# EMA Hourly Continuation — DODO/USDT P89_100

**Symbol:** DODO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.2188 |
| net_win_rate | 0.3495 |
| gross_profit_factor | 0.5962 |
| gross_win_rate | 0.3967 |
| sharpe_ratio | -10.7911 |
| sortino_ratio | -4.2067 |
| max_drawdown | 0.9959 |
| cagr | -0.8858 |
| net_avg_win | 11.0680 |
| net_avg_loss | -27.1795 |
| avg_hold_time_bars | 2.3897 |
| exposure | 0.0780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
