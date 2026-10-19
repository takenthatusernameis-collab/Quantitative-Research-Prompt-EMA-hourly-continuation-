# EMA Hourly Continuation — XMR/USDT P144_200

**Symbol:** XMR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.2447 |
| net_win_rate | 0.3699 |
| gross_profit_factor | 0.6542 |
| gross_win_rate | 0.3866 |
| sharpe_ratio | -9.8128 |
| sortino_ratio | -3.6413 |
| max_drawdown | 0.9910 |
| cagr | -0.8464 |
| net_avg_win | 13.2152 |
| net_avg_loss | -31.6926 |
| avg_hold_time_bars | 2.9985 |
| exposure | 0.0895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
