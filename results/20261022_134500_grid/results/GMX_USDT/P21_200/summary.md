# EMA Hourly Continuation — GMX/USDT P21_200

**Symbol:** GMX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.7142 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9709 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.5958 |
| sortino_ratio | -0.8001 |
| max_drawdown | 0.6606 |
| cagr | -0.3123 |
| net_avg_win | 67.0817 |
| net_avg_loss | -86.3219 |
| avg_hold_time_bars | 26.9430 |
| exposure | 0.5805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
