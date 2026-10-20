# EMA Hourly Continuation — XAI/USDT P8_34

**Symbol:** XAI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1459 |
| net_profit_factor | 0.6302 |
| net_win_rate | 0.4256 |
| gross_profit_factor | 0.9955 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -8.9253 |
| sortino_ratio | -4.7915 |
| max_drawdown | 0.9974 |
| cagr | -0.9033 |
| net_avg_win | 27.3613 |
| net_avg_loss | -32.1755 |
| avg_hold_time_bars | 5.3263 |
| exposure | 0.3532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
