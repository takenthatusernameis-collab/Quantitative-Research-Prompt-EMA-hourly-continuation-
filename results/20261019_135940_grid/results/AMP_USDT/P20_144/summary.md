# EMA Hourly Continuation — AMP/USDT P20_144

**Symbol:** AMP/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 824 |
| net_profit_factor | 0.3624 |
| net_win_rate | 0.3883 |
| gross_profit_factor | 0.6114 |
| gross_win_rate | 0.3981 |
| sharpe_ratio | -8.1793 |
| sortino_ratio | -3.2950 |
| max_drawdown | 0.9840 |
| cagr | -0.8045 |
| net_avg_win | 17.4687 |
| net_avg_loss | -30.6034 |
| avg_hold_time_bars | 14.0692 |
| exposure | 0.5270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
