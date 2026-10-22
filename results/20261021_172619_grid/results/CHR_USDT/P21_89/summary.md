# EMA Hourly Continuation — CHR/USDT P21_89

**Symbol:** CHR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.7247 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8931 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -2.5501 |
| sortino_ratio | -0.8416 |
| max_drawdown | 0.6655 |
| cagr | -0.3214 |
| net_avg_win | 65.1971 |
| net_avg_loss | -78.4426 |
| avg_hold_time_bars | 15.1146 |
| exposure | 0.3700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
