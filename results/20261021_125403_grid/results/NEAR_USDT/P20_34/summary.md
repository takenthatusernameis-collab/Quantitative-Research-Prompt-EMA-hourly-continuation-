# EMA Hourly Continuation — NEAR/USDT P20_34

**Symbol:** NEAR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.8414 |
| net_win_rate | 0.5316 |
| gross_profit_factor | 1.1191 |
| gross_win_rate | 0.5316 |
| sharpe_ratio | -0.8252 |
| sortino_ratio | -0.1955 |
| max_drawdown | 0.2570 |
| cagr | -0.0871 |
| net_avg_win | 75.8687 |
| net_avg_loss | -102.3398 |
| avg_hold_time_bars | 5.5688 |
| exposure | 0.0681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
