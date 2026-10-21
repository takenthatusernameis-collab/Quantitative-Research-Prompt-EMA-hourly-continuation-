# EMA Hourly Continuation — API3/USDT P20_26

**Symbol:** API3/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.6328 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.9049 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -2.3260 |
| sortino_ratio | -0.5178 |
| max_drawdown | 0.4872 |
| cagr | -0.2112 |
| net_avg_win | 67.8458 |
| net_avg_loss | -95.4945 |
| avg_hold_time_bars | 5.2479 |
| exposure | 0.0577 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
