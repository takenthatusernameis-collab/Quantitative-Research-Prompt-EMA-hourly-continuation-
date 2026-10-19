# EMA Hourly Continuation — TRX/USDT P144_200

**Symbol:** TRX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.1637 |
| net_win_rate | 0.3230 |
| gross_profit_factor | 0.7977 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -8.9986 |
| sortino_ratio | -2.6070 |
| max_drawdown | 0.9736 |
| cagr | -0.7627 |
| net_avg_win | 16.5586 |
| net_avg_loss | -48.2750 |
| avg_hold_time_bars | 4.4831 |
| exposure | 0.0725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
