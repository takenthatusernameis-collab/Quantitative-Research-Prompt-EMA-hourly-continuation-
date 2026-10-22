# EMA Hourly Continuation — OP/USDT P50_144

**Symbol:** OP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.6010 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8929 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -3.4697 |
| sortino_ratio | -1.0452 |
| max_drawdown | 0.7139 |
| cagr | -0.3866 |
| net_avg_win | 50.7050 |
| net_avg_loss | -72.6147 |
| avg_hold_time_bars | 15.3128 |
| exposure | 0.3160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
