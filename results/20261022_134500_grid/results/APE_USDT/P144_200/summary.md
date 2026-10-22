# EMA Hourly Continuation — APE/USDT P144_200

**Symbol:** APE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.5111 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9247 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -4.1590 |
| sortino_ratio | -1.2386 |
| max_drawdown | 0.7880 |
| cagr | -0.4554 |
| net_avg_win | 38.2382 |
| net_avg_loss | -68.4161 |
| avg_hold_time_bars | 3.8884 |
| exposure | 0.0792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
