# EMA Hourly Continuation — APE/USDT P21_144

**Symbol:** APE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.6672 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9521 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -2.5085 |
| sortino_ratio | -0.7886 |
| max_drawdown | 0.6258 |
| cagr | -0.3120 |
| net_avg_win | 49.8346 |
| net_avg_loss | -72.9069 |
| avg_hold_time_bars | 23.3831 |
| exposure | 0.5272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
