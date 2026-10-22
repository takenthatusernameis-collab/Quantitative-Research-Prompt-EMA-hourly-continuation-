# EMA Hourly Continuation — TWT/USDT P20_89

**Symbol:** TWT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 814 |
| net_profit_factor | 0.5446 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.9572 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -5.3755 |
| sortino_ratio | -2.1569 |
| max_drawdown | 0.9342 |
| cagr | -0.6500 |
| net_avg_win | 28.9905 |
| net_avg_loss | -47.3019 |
| avg_hold_time_bars | 10.2248 |
| exposure | 0.3783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
