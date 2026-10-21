# EMA Hourly Continuation — BIGTIME/USDT P26_144

**Symbol:** BIGTIME/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.9012 |
| net_win_rate | 0.5242 |
| gross_profit_factor | 1.0968 |
| gross_win_rate | 0.5242 |
| sharpe_ratio | -0.6095 |
| sortino_ratio | -0.1737 |
| max_drawdown | 0.2534 |
| cagr | -0.0802 |
| net_avg_win | 84.1945 |
| net_avg_loss | -102.9163 |
| avg_hold_time_bars | 27.3766 |
| exposure | 0.4869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
