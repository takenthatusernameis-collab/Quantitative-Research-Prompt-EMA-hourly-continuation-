# EMA Hourly Continuation — SUI/USDT P21_200

**Symbol:** SUI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.9219 |
| net_win_rate | 0.5184 |
| gross_profit_factor | 1.0697 |
| gross_win_rate | 0.5184 |
| sharpe_ratio | -0.3681 |
| sortino_ratio | -0.0874 |
| max_drawdown | 0.2180 |
| cagr | -0.0427 |
| net_avg_win | 86.9190 |
| net_avg_loss | -101.4814 |
| avg_hold_time_bars | 50.6360 |
| exposure | 0.6260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
