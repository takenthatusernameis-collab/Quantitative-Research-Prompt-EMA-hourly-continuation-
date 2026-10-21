# EMA Hourly Continuation — MANA/USDT P12_26

**Symbol:** MANA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6438 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9303 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -2.9030 |
| sortino_ratio | -0.9052 |
| max_drawdown | 0.6493 |
| cagr | -0.3388 |
| net_avg_win | 50.9954 |
| net_avg_loss | -74.6482 |
| avg_hold_time_bars | 4.8453 |
| exposure | 0.1040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
