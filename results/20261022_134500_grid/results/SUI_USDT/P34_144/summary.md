# EMA Hourly Continuation — SUI/USDT P34_144

**Symbol:** SUI/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.6764 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 1.0201 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -3.1149 |
| sortino_ratio | -1.0038 |
| max_drawdown | 0.7429 |
| cagr | -0.3866 |
| net_avg_win | 56.8208 |
| net_avg_loss | -81.5008 |
| avg_hold_time_bars | 14.8068 |
| exposure | 0.3554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
