# EMA Hourly Continuation — G/USDT P21_100

**Symbol:** G/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.5550 |
| net_win_rate | 0.4237 |
| gross_profit_factor | 0.7132 |
| gross_win_rate | 0.4237 |
| sharpe_ratio | -3.6755 |
| sortino_ratio | -1.0902 |
| max_drawdown | 0.6949 |
| cagr | -0.3955 |
| net_avg_win | 51.4941 |
| net_avg_loss | -68.2082 |
| avg_hold_time_bars | 24.4421 |
| exposure | 0.4884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
