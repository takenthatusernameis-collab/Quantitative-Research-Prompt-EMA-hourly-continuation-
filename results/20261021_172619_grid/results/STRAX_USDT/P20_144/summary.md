# EMA Hourly Continuation — STRAX/USDT P20_144

**Symbol:** STRAX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.6330 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.8189 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -3.5615 |
| sortino_ratio | -1.1625 |
| max_drawdown | 0.7429 |
| cagr | -0.4158 |
| net_avg_win | 54.2022 |
| net_avg_loss | -68.6822 |
| avg_hold_time_bars | 18.8371 |
| exposure | 0.4547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
