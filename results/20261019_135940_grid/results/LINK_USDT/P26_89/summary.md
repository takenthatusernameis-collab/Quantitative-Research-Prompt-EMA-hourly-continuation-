# EMA Hourly Continuation — LINK/USDT P26_89

**Symbol:** LINK/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.5881 |
| net_win_rate | 0.4617 |
| gross_profit_factor | 0.9412 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -5.0331 |
| sortino_ratio | -1.8009 |
| max_drawdown | 0.8940 |
| cagr | -0.5843 |
| net_avg_win | 42.1978 |
| net_avg_loss | -61.5342 |
| avg_hold_time_bars | 10.1227 |
| exposure | 0.3000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
