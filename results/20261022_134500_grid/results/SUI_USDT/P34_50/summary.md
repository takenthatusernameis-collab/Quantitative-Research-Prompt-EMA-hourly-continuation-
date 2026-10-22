# EMA Hourly Continuation — SUI/USDT P34_50

**Symbol:** SUI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 950 |
| net_profit_factor | 0.4275 |
| net_win_rate | 0.4168 |
| gross_profit_factor | 0.8535 |
| gross_win_rate | 0.4358 |
| sharpe_ratio | -9.6435 |
| sortino_ratio | -4.2045 |
| max_drawdown | 0.9957 |
| cagr | -0.8846 |
| net_avg_win | 18.7709 |
| net_avg_loss | -31.3883 |
| avg_hold_time_bars | 2.4863 |
| exposure | 0.1074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
