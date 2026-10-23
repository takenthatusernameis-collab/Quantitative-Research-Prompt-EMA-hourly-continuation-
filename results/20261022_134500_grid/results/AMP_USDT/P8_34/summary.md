# EMA Hourly Continuation — AMP/USDT P8_34

**Symbol:** AMP/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1783 |
| net_profit_factor | 0.3057 |
| net_win_rate | 0.3780 |
| gross_profit_factor | 0.6455 |
| gross_win_rate | 0.3988 |
| sharpe_ratio | -14.5339 |
| sortino_ratio | -8.6576 |
| max_drawdown | 1.0000 |
| cagr | -0.9878 |
| net_avg_win | 6.5314 |
| net_avg_loss | -12.9865 |
| avg_hold_time_bars | 4.2154 |
| exposure | 0.3416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
