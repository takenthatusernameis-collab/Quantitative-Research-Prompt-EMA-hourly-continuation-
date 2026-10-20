# EMA Hourly Continuation — TNSR/USDT P8_144

**Symbol:** TNSR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.7142 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.9651 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -2.8746 |
| sortino_ratio | -0.9117 |
| max_drawdown | 0.7017 |
| cagr | -0.3551 |
| net_avg_win | 68.5406 |
| net_avg_loss | -85.7735 |
| avg_hold_time_bars | 30.9749 |
| exposure | 0.7247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
