# EMA Hourly Continuation — TIA/USDT P12_34

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.7966 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0049 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -1.5251 |
| sortino_ratio | -0.5188 |
| max_drawdown | 0.5292 |
| cagr | -0.2134 |
| net_avg_win | 62.2249 |
| net_avg_loss | -80.6559 |
| avg_hold_time_bars | 7.5062 |
| exposure | 0.1914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
