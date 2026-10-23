# EMA Hourly Continuation — DEEP/USDT P8_144

**Symbol:** DEEP/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.6655 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.8501 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -2.7493 |
| sortino_ratio | -0.8183 |
| max_drawdown | 0.5539 |
| cagr | -0.3225 |
| net_avg_win | 64.8130 |
| net_avg_loss | -83.4000 |
| avg_hold_time_bars | 37.3149 |
| exposure | 0.7648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
