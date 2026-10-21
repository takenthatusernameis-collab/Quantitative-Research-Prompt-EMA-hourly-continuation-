# EMA Hourly Continuation — LSK/USDT P12_89

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.7383 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9597 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -2.3109 |
| sortino_ratio | -0.7538 |
| max_drawdown | 0.6118 |
| cagr | -0.2939 |
| net_avg_win | 64.7162 |
| net_avg_loss | -82.7706 |
| avg_hold_time_bars | 22.1243 |
| exposure | 0.5260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
