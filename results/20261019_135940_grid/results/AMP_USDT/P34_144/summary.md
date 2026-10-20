# EMA Hourly Continuation — AMP/USDT P34_144

**Symbol:** AMP/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 722 |
| net_profit_factor | 0.3634 |
| net_win_rate | 0.3781 |
| gross_profit_factor | 0.6554 |
| gross_win_rate | 0.4017 |
| sharpe_ratio | -7.8301 |
| sortino_ratio | -2.9572 |
| max_drawdown | 0.9754 |
| cagr | -0.7680 |
| net_avg_win | 20.3760 |
| net_avg_loss | -34.0927 |
| avg_hold_time_bars | 13.2742 |
| exposure | 0.4356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
