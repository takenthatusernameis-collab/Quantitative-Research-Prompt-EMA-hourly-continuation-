# EMA Hourly Continuation — TAIKO/USDT P50_89

**Symbol:** TAIKO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.6141 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.8535 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -2.5890 |
| sortino_ratio | -0.6804 |
| max_drawdown | 0.5288 |
| cagr | -0.2673 |
| net_avg_win | 55.0511 |
| net_avg_loss | -80.1005 |
| avg_hold_time_bars | 8.2219 |
| exposure | 0.1264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
