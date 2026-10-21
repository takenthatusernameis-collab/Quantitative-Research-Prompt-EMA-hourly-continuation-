# EMA Hourly Continuation — WLD/USDT P26_89

**Symbol:** WLD/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.9860 |
| net_win_rate | 0.5427 |
| gross_profit_factor | 1.1742 |
| gross_win_rate | 0.5427 |
| sharpe_ratio | -0.0286 |
| sortino_ratio | -0.0085 |
| max_drawdown | 0.2048 |
| cagr | -0.0120 |
| net_avg_win | 91.7535 |
| net_avg_loss | -110.4131 |
| avg_hold_time_bars | 15.1019 |
| exposure | 0.2897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
