# EMA Hourly Continuation — DBR/USDT P12_20

**Symbol:** DBR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 905 |
| net_profit_factor | 0.3612 |
| net_win_rate | 0.3779 |
| gross_profit_factor | 0.9421 |
| gross_win_rate | 0.4398 |
| sharpe_ratio | -12.6995 |
| sortino_ratio | -6.1421 |
| max_drawdown | 0.9984 |
| cagr | -0.9593 |
| net_avg_win | 16.5035 |
| net_avg_loss | -27.7584 |
| avg_hold_time_bars | 3.6420 |
| exposure | 0.1874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
