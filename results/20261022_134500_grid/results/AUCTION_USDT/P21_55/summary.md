# EMA Hourly Continuation — AUCTION/USDT P21_55

**Symbol:** AUCTION/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 899 |
| net_profit_factor | 0.4821 |
| net_win_rate | 0.4305 |
| gross_profit_factor | 0.8451 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -7.7062 |
| sortino_ratio | -3.2529 |
| max_drawdown | 0.9829 |
| cagr | -0.7979 |
| net_avg_win | 23.6302 |
| net_avg_loss | -37.0462 |
| avg_hold_time_bars | 6.5684 |
| exposure | 0.2673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
