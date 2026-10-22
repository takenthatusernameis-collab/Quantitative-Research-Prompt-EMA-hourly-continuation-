# EMA Hourly Continuation — APE/USDT P55_200

**Symbol:** APE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.6991 |
| net_win_rate | 0.5107 |
| gross_profit_factor | 1.0212 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -1.9820 |
| sortino_ratio | -0.5792 |
| max_drawdown | 0.4960 |
| cagr | -0.2375 |
| net_avg_win | 53.3734 |
| net_avg_loss | -79.6764 |
| avg_hold_time_bars | 18.9454 |
| exposure | 0.3625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
