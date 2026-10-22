# EMA Hourly Continuation — TRX/USDT P34_89

**Symbol:** TRX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.2578 |
| net_win_rate | 0.3536 |
| gross_profit_factor | 0.9208 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -10.4936 |
| sortino_ratio | -3.8625 |
| max_drawdown | 0.9944 |
| cagr | -0.8731 |
| net_avg_win | 15.6305 |
| net_avg_loss | -33.1642 |
| avg_hold_time_bars | 7.5744 |
| exposure | 0.2152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
