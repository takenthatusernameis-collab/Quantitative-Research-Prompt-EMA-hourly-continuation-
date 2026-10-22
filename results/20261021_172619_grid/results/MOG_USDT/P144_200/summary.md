# EMA Hourly Continuation — MOG/USDT P144_200

**Symbol:** MOG/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 190 |
| net_profit_factor | 0.8917 |
| net_win_rate | 0.5263 |
| gross_profit_factor | 1.0989 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -0.4762 |
| sortino_ratio | -0.0990 |
| max_drawdown | 0.1531 |
| cagr | -0.0465 |
| net_avg_win | 85.2205 |
| net_avg_loss | -106.1927 |
| avg_hold_time_bars | 7.8211 |
| exposure | 0.0739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
