# EMA Hourly Continuation — MASK/USDT P20_26

**Symbol:** MASK/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.6506 |
| net_win_rate | 0.5169 |
| gross_profit_factor | 1.1040 |
| gross_win_rate | 0.5236 |
| sharpe_ratio | -2.2733 |
| sortino_ratio | -0.5611 |
| max_drawdown | 0.5023 |
| cagr | -0.2280 |
| net_avg_win | 58.1530 |
| net_avg_loss | -95.6381 |
| avg_hold_time_bars | 6.2872 |
| exposure | 0.0846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
