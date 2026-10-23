# EMA Hourly Continuation — VR/USDT P55_144

**Symbol:** VR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.3647 |
| net_win_rate | 0.3078 |
| gross_profit_factor | 0.5707 |
| gross_win_rate | 0.3214 |
| sharpe_ratio | -9.9859 |
| sortino_ratio | -3.3995 |
| max_drawdown | 0.9925 |
| cagr | -0.8576 |
| net_avg_win | 31.4825 |
| net_avg_loss | -38.3870 |
| avg_hold_time_bars | 9.0901 |
| exposure | 0.2430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
