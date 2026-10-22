# EMA Hourly Continuation — CHR/USDT P26_144

**Symbol:** CHR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.7755 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 0.9419 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -1.6002 |
| sortino_ratio | -0.4602 |
| max_drawdown | 0.4431 |
| cagr | -0.1915 |
| net_avg_win | 72.3926 |
| net_avg_loss | -88.0175 |
| avg_hold_time_bars | 26.1838 |
| exposure | 0.4834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
