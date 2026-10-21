# EMA Hourly Continuation — SHIB/USDT P20_26

**Symbol:** SHIB/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 146 |
| net_profit_factor | 0.7430 |
| net_win_rate | 0.5205 |
| gross_profit_factor | 1.0844 |
| gross_win_rate | 0.5205 |
| sharpe_ratio | -1.1345 |
| sortino_ratio | -0.1978 |
| max_drawdown | 0.2938 |
| cagr | -0.0870 |
| net_avg_win | 77.6886 |
| net_avg_loss | -113.5254 |
| avg_hold_time_bars | 4.0685 |
| exposure | 0.0270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
