# EMA Hourly Continuation — AVAX/USDT P26_34

**Symbol:** AVAX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 160 |
| net_profit_factor | 0.6782 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 0.9766 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -1.6461 |
| sortino_ratio | -0.2990 |
| max_drawdown | 0.3538 |
| cagr | -0.1277 |
| net_avg_win | 78.4517 |
| net_avg_loss | -110.0317 |
| avg_hold_time_bars | 4.0187 |
| exposure | 0.0292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
