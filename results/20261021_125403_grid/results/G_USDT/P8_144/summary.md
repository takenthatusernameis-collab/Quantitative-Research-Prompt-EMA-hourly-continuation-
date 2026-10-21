# EMA Hourly Continuation — G/USDT P8_144

**Symbol:** G/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.8648 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0486 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -0.7849 |
| sortino_ratio | -0.2045 |
| max_drawdown | 0.3893 |
| cagr | -0.0920 |
| net_avg_win | 82.8315 |
| net_avg_loss | -100.6058 |
| avg_hold_time_bars | 51.9298 |
| exposure | 0.7782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
