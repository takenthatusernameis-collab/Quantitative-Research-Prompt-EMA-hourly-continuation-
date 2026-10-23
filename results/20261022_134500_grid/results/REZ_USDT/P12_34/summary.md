# EMA Hourly Continuation — REZ/USDT P12_34

**Symbol:** REZ/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1180 |
| net_profit_factor | 0.6060 |
| net_win_rate | 0.4653 |
| gross_profit_factor | 0.9732 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -6.2626 |
| sortino_ratio | -3.0574 |
| max_drawdown | 0.9734 |
| cagr | -0.7676 |
| net_avg_win | 27.2561 |
| net_avg_loss | -39.1336 |
| avg_hold_time_bars | 4.8263 |
| exposure | 0.2627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
