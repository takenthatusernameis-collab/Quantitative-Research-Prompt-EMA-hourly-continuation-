# EMA Hourly Continuation — VR/USDT P21_34

**Symbol:** VR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.6399 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9584 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -2.3674 |
| sortino_ratio | -0.5154 |
| max_drawdown | 0.4537 |
| cagr | -0.2132 |
| net_avg_win | 71.7718 |
| net_avg_loss | -102.1380 |
| avg_hold_time_bars | 8.3830 |
| exposure | 0.0895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
