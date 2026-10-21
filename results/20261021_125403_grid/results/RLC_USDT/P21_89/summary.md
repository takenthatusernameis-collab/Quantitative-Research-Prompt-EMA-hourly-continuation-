# EMA Hourly Continuation — RLC/USDT P21_89

**Symbol:** RLC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.8106 |
| net_win_rate | 0.5130 |
| gross_profit_factor | 1.0485 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -1.5820 |
| sortino_ratio | -0.5276 |
| max_drawdown | 0.5067 |
| cagr | -0.2166 |
| net_avg_win | 70.7848 |
| net_avg_loss | -91.9772 |
| avg_hold_time_bars | 13.3815 |
| exposure | 0.3285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
