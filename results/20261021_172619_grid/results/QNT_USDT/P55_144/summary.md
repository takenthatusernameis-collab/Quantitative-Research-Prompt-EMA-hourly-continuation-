# EMA Hourly Continuation — QNT/USDT P55_144

**Symbol:** QNT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.6570 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.8945 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -2.6487 |
| sortino_ratio | -0.7642 |
| max_drawdown | 0.6079 |
| cagr | -0.2948 |
| net_avg_win | 57.9754 |
| net_avg_loss | -79.2091 |
| avg_hold_time_bars | 11.4363 |
| exposure | 0.2121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
