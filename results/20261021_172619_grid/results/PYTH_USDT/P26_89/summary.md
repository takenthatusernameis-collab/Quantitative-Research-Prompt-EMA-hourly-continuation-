# EMA Hourly Continuation — PYTH/USDT P26_89

**Symbol:** PYTH/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.7007 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8586 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -2.3869 |
| sortino_ratio | -0.7262 |
| max_drawdown | 0.5801 |
| cagr | -0.2839 |
| net_avg_win | 62.6862 |
| net_avg_loss | -77.0979 |
| avg_hold_time_bars | 12.7773 |
| exposure | 0.2660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
