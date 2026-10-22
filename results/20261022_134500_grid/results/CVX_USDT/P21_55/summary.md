# EMA Hourly Continuation — CVX/USDT P21_55

**Symbol:** CVX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 934 |
| net_profit_factor | 0.4744 |
| net_win_rate | 0.4304 |
| gross_profit_factor | 0.7691 |
| gross_win_rate | 0.4433 |
| sharpe_ratio | -6.9998 |
| sortino_ratio | -3.0154 |
| max_drawdown | 0.9753 |
| cagr | -0.7696 |
| net_avg_win | 21.8876 |
| net_avg_loss | -34.8648 |
| avg_hold_time_bars | 5.2880 |
| exposure | 0.2245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
