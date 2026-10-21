# EMA Hourly Continuation — AVAX/USDT P26_200

**Symbol:** AVAX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.9003 |
| net_win_rate | 0.5234 |
| gross_profit_factor | 1.0897 |
| gross_win_rate | 0.5234 |
| sharpe_ratio | -0.4683 |
| sortino_ratio | -0.1034 |
| max_drawdown | 0.2503 |
| cagr | -0.0487 |
| net_avg_win | 86.4931 |
| net_avg_loss | -105.5083 |
| avg_hold_time_bars | 53.9149 |
| exposure | 0.5759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
