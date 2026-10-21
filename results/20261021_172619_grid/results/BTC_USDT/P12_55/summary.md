# EMA Hourly Continuation — BTC/USDT P12_55

**Symbol:** BTC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.5859 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9632 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.8651 |
| sortino_ratio | -1.3032 |
| max_drawdown | 0.8199 |
| cagr | -0.4495 |
| net_avg_win | 37.4565 |
| net_avg_loss | -62.3155 |
| avg_hold_time_bars | 14.0671 |
| exposure | 0.3522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
