# EMA Hourly Continuation — MNT/USDT P20_34

**Symbol:** MNT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1105 |
| net_profit_factor | 0.2521 |
| net_win_rate | 0.3882 |
| gross_profit_factor | 0.7331 |
| gross_win_rate | 0.4271 |
| sharpe_ratio | -12.7832 |
| sortino_ratio | -6.1143 |
| max_drawdown | 0.9997 |
| cagr | -0.9607 |
| net_avg_win | 7.8546 |
| net_avg_loss | -19.7732 |
| avg_hold_time_bars | 3.1231 |
| exposure | 0.1569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
