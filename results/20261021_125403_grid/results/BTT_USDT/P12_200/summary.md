# EMA Hourly Continuation — BTT/USDT P12_200

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.6512 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -2.0323 |
| sortino_ratio | -0.4553 |
| max_drawdown | 0.4605 |
| cagr | -0.1906 |
| net_avg_win | 65.2110 |
| net_avg_loss | -90.8906 |
| avg_hold_time_bars | 68.5726 |
| exposure | 0.7730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
