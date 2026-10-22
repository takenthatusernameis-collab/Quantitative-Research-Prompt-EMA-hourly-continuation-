# EMA Hourly Continuation — DAG/USDT P21_144

**Symbol:** DAG/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.7706 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.8940 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -1.4940 |
| sortino_ratio | -0.4263 |
| max_drawdown | 0.4263 |
| cagr | -0.1793 |
| net_avg_win | 68.4653 |
| net_avg_loss | -81.2273 |
| avg_hold_time_bars | 24.3483 |
| exposure | 0.4449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
