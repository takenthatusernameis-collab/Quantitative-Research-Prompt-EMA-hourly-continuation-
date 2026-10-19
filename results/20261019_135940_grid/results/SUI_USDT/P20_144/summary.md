# EMA Hourly Continuation — SUI/USDT P20_144

**Symbol:** SUI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.7083 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 1.0475 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -2.7679 |
| sortino_ratio | -0.9067 |
| max_drawdown | 0.6971 |
| cagr | -0.3548 |
| net_avg_win | 60.0149 |
| net_avg_loss | -83.1873 |
| avg_hold_time_bars | 19.9927 |
| exposure | 0.4953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
