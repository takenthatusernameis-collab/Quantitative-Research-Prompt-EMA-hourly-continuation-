# EMA Hourly Continuation — TRADE/USDT P8_89

**Symbol:** TRADE/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.6174 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.8482 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -3.7465 |
| sortino_ratio | -1.3785 |
| max_drawdown | 0.8185 |
| cagr | -0.4849 |
| net_avg_win | 41.2820 |
| net_avg_loss | -57.1322 |
| avg_hold_time_bars | 18.9593 |
| exposure | 0.5929 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
