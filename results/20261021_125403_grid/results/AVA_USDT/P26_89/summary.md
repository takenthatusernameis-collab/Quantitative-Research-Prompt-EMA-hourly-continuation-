# EMA Hourly Continuation — AVA/USDT P26_89

**Symbol:** AVA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.9558 |
| net_win_rate | 0.5548 |
| gross_profit_factor | 1.2254 |
| gross_win_rate | 0.5548 |
| sharpe_ratio | -0.2182 |
| sortino_ratio | -0.0677 |
| max_drawdown | 0.3339 |
| cagr | -0.0376 |
| net_avg_win | 78.3954 |
| net_avg_loss | -102.2225 |
| avg_hold_time_bars | 13.5022 |
| exposure | 0.2799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
