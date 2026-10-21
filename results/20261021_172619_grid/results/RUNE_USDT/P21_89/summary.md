# EMA Hourly Continuation — RUNE/USDT P21_89

**Symbol:** RUNE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.8235 |
| net_win_rate | 0.5167 |
| gross_profit_factor | 1.0509 |
| gross_win_rate | 0.5167 |
| sharpe_ratio | -1.1358 |
| sortino_ratio | -0.3221 |
| max_drawdown | 0.3666 |
| cagr | -0.1392 |
| net_avg_win | 72.8085 |
| net_avg_loss | -94.5304 |
| avg_hold_time_bars | 27.2879 |
| exposure | 0.4825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
