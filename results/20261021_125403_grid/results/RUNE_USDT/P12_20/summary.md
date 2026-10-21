# EMA Hourly Continuation — RUNE/USDT P12_20

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.6220 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9184 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -2.4720 |
| sortino_ratio | -0.5831 |
| max_drawdown | 0.4892 |
| cagr | -0.2347 |
| net_avg_win | 62.4116 |
| net_avg_loss | -91.1494 |
| avg_hold_time_bars | 4.3469 |
| exposure | 0.0535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
