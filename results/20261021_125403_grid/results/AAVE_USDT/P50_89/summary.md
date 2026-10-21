# EMA Hourly Continuation — AAVE/USDT P50_89

**Symbol:** AAVE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.9113 |
| net_win_rate | 0.5514 |
| gross_profit_factor | 1.2174 |
| gross_win_rate | 0.5514 |
| sharpe_ratio | -0.4790 |
| sortino_ratio | -0.1247 |
| max_drawdown | 0.2681 |
| cagr | -0.0587 |
| net_avg_win | 81.7899 |
| net_avg_loss | -110.3241 |
| avg_hold_time_bars | 7.0436 |
| exposure | 0.1028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
