# EMA Hourly Continuation — XEC/USDT P8_20

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1684 |
| net_profit_factor | 0.3584 |
| net_win_rate | 0.4091 |
| gross_profit_factor | 0.8797 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -13.8828 |
| sortino_ratio | -8.0887 |
| max_drawdown | 1.0000 |
| cagr | -0.9838 |
| net_avg_win | 8.1074 |
| net_avg_loss | -15.6640 |
| avg_hold_time_bars | 3.2726 |
| exposure | 0.2494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
