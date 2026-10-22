# EMA Hourly Continuation — BDX/USDT P12_50

**Symbol:** BDX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1504 |
| net_profit_factor | 0.2861 |
| net_win_rate | 0.2779 |
| gross_profit_factor | 0.7077 |
| gross_win_rate | 0.3404 |
| sharpe_ratio | -19.9967 |
| sortino_ratio | -11.6282 |
| max_drawdown | 1.0000 |
| cagr | -0.9983 |
| net_avg_win | 9.5876 |
| net_avg_loss | -12.8984 |
| avg_hold_time_bars | 4.1955 |
| exposure | 0.2868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
