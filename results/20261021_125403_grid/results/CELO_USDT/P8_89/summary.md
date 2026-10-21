# EMA Hourly Continuation — CELO/USDT P8_89

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.9176 |
| net_win_rate | 0.5274 |
| gross_profit_factor | 1.1214 |
| gross_win_rate | 0.5274 |
| sharpe_ratio | -0.6542 |
| sortino_ratio | -0.2164 |
| max_drawdown | 0.4033 |
| cagr | -0.0999 |
| net_avg_win | 93.1156 |
| net_avg_loss | -113.2483 |
| avg_hold_time_bars | 26.8185 |
| exposure | 0.6420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
