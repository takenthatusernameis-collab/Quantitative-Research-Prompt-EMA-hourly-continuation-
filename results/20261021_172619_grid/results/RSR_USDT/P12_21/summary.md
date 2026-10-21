# EMA Hourly Continuation — RSR/USDT P12_21

**Symbol:** RSR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.8028 |
| net_win_rate | 0.5184 |
| gross_profit_factor | 1.0628 |
| gross_win_rate | 0.5184 |
| sharpe_ratio | -1.1350 |
| sortino_ratio | -0.2828 |
| max_drawdown | 0.3444 |
| cagr | -0.1221 |
| net_avg_win | 73.2349 |
| net_avg_loss | -98.1954 |
| avg_hold_time_bars | 5.5017 |
| exposure | 0.0748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
