# EMA Hourly Continuation — WEMIX/USDT P34_50

**Symbol:** WEMIX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1432 |
| net_profit_factor | 0.0821 |
| net_win_rate | 0.2409 |
| gross_profit_factor | 0.2404 |
| gross_win_rate | 0.2793 |
| sharpe_ratio | -19.9682 |
| sortino_ratio | -11.2376 |
| max_drawdown | 1.0000 |
| cagr | -0.9976 |
| net_avg_win | 2.5929 |
| net_avg_loss | -10.0226 |
| avg_hold_time_bars | 2.5265 |
| exposure | 0.1645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
