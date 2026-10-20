# EMA Hourly Continuation — MTL/USDT P21_34

**Symbol:** MTL/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.3021 |
| net_win_rate | 0.3883 |
| gross_profit_factor | 0.7597 |
| gross_win_rate | 0.4330 |
| sharpe_ratio | -11.7612 |
| sortino_ratio | -5.4995 |
| max_drawdown | 0.9992 |
| cagr | -0.9419 |
| net_avg_win | 10.3703 |
| net_avg_loss | -21.7912 |
| avg_hold_time_bars | 3.5847 |
| exposure | 0.1742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
