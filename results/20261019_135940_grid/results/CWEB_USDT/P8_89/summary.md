# EMA Hourly Continuation — CWEB/USDT P8_89

**Symbol:** CWEB/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.5324 |
| net_win_rate | 0.4229 |
| gross_profit_factor | 0.8267 |
| gross_win_rate | 0.4247 |
| sharpe_ratio | -5.5247 |
| sortino_ratio | -1.8195 |
| max_drawdown | 0.9026 |
| cagr | -0.5992 |
| net_avg_win | 43.3891 |
| net_avg_loss | -59.7304 |
| avg_hold_time_bars | 26.7527 |
| exposure | 0.6785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
