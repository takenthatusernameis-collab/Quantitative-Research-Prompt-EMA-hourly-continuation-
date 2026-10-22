# EMA Hourly Continuation — VET/USDT P26_55

**Symbol:** VET/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 917 |
| net_profit_factor | 0.4860 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.9540 |
| gross_win_rate | 0.4809 |
| sharpe_ratio | -7.3031 |
| sortino_ratio | -3.1383 |
| max_drawdown | 0.9795 |
| cagr | -0.7836 |
| net_avg_win | 21.9772 |
| net_avg_loss | -38.3836 |
| avg_hold_time_bars | 3.9793 |
| exposure | 0.1659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
