# EMA Hourly Continuation — TAIKO/USDT P8_89

**Symbol:** TAIKO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.8098 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 0.9929 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -1.5100 |
| sortino_ratio | -0.5034 |
| max_drawdown | 0.5007 |
| cagr | -0.2079 |
| net_avg_win | 70.4637 |
| net_avg_loss | -87.3512 |
| avg_hold_time_bars | 24.7797 |
| exposure | 0.6106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
