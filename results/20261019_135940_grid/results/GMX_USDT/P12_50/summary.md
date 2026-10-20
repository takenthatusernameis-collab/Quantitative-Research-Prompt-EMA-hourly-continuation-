# EMA Hourly Continuation — GMX/USDT P12_50

**Symbol:** GMX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1037 |
| net_profit_factor | 0.5073 |
| net_win_rate | 0.4272 |
| gross_profit_factor | 0.8435 |
| gross_win_rate | 0.4388 |
| sharpe_ratio | -7.4724 |
| sortino_ratio | -3.3782 |
| max_drawdown | 0.9843 |
| cagr | -0.8070 |
| net_avg_win | 22.8680 |
| net_avg_loss | -33.6194 |
| avg_hold_time_bars | 7.9990 |
| exposure | 0.3770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
