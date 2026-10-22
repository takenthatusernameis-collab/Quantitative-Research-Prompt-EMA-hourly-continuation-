# EMA Hourly Continuation — XDC/USDT P12_21

**Symbol:** XDC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1460 |
| net_profit_factor | 0.1192 |
| net_win_rate | 0.3062 |
| gross_profit_factor | 0.4945 |
| gross_win_rate | 0.3966 |
| sharpe_ratio | -18.8529 |
| sortino_ratio | -10.7665 |
| max_drawdown | 1.0000 |
| cagr | -0.9975 |
| net_avg_win | 3.0267 |
| net_avg_loss | -11.2073 |
| avg_hold_time_bars | 2.5644 |
| exposure | 0.1702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
