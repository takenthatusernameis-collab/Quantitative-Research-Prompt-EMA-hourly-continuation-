# EMA Hourly Continuation — MASK/USDT P8_144

**Symbol:** MASK/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6319 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8190 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -2.6872 |
| sortino_ratio | -0.7995 |
| max_drawdown | 0.6177 |
| cagr | -0.3077 |
| net_avg_win | 50.9818 |
| net_avg_loss | -69.6907 |
| avg_hold_time_bars | 35.6667 |
| exposure | 0.7101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
