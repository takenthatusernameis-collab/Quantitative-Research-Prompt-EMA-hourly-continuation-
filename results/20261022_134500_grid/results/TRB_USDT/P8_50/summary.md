# EMA Hourly Continuation — TRB/USDT P8_50

**Symbol:** TRB/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1140 |
| net_profit_factor | 0.4699 |
| net_win_rate | 0.4263 |
| gross_profit_factor | 0.7913 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -8.3508 |
| sortino_ratio | -3.9282 |
| max_drawdown | 0.9930 |
| cagr | -0.8589 |
| net_avg_win | 18.1077 |
| net_avg_loss | -28.6373 |
| avg_hold_time_bars | 9.2772 |
| exposure | 0.4786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
