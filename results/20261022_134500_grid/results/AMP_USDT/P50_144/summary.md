# EMA Hourly Continuation — AMP/USDT P50_144

**Symbol:** AMP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.3410 |
| net_win_rate | 0.3830 |
| gross_profit_factor | 0.6223 |
| gross_win_rate | 0.3995 |
| sharpe_ratio | -8.0339 |
| sortino_ratio | -3.0403 |
| max_drawdown | 0.9794 |
| cagr | -0.7839 |
| net_avg_win | 18.0848 |
| net_avg_loss | -32.9277 |
| avg_hold_time_bars | 9.4542 |
| exposure | 0.3141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
