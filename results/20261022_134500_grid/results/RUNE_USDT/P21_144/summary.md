# EMA Hourly Continuation — RUNE/USDT P21_144

**Symbol:** RUNE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7834 |
| net_win_rate | 0.5224 |
| gross_profit_factor | 1.0946 |
| gross_win_rate | 0.5277 |
| sharpe_ratio | -1.3964 |
| sortino_ratio | -0.3873 |
| max_drawdown | 0.4059 |
| cagr | -0.1669 |
| net_avg_win | 67.2094 |
| net_avg_loss | -93.8464 |
| avg_hold_time_bars | 37.1055 |
| exposure | 0.6392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
