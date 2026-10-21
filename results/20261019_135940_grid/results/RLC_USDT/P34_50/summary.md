# EMA Hourly Continuation — RLC/USDT P34_50

**Symbol:** RLC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 887 |
| net_profit_factor | 0.3817 |
| net_win_rate | 0.4397 |
| gross_profit_factor | 0.8428 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -8.5315 |
| sortino_ratio | -3.5943 |
| max_drawdown | 0.9899 |
| cagr | -0.8378 |
| net_avg_win | 15.6653 |
| net_avg_loss | -32.2045 |
| avg_hold_time_bars | 3.1037 |
| exposure | 0.1251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
