# EMA Hourly Continuation — KMNO/USDT P50_89

**Symbol:** KMNO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.7067 |
| net_win_rate | 0.4860 |
| gross_profit_factor | 0.9247 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -1.8638 |
| sortino_ratio | -0.4804 |
| max_drawdown | 0.4265 |
| cagr | -0.1983 |
| net_avg_win | 65.0188 |
| net_avg_loss | -86.9888 |
| avg_hold_time_bars | 9.2087 |
| exposure | 0.1365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
