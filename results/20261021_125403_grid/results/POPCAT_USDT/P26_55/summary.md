# EMA Hourly Continuation — POPCAT/USDT P26_55

**Symbol:** POPCAT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.7044 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.8904 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -2.7236 |
| sortino_ratio | -0.8572 |
| max_drawdown | 0.5818 |
| cagr | -0.3262 |
| net_avg_win | 69.7820 |
| net_avg_loss | -86.2968 |
| avg_hold_time_bars | 6.7197 |
| exposure | 0.1494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
