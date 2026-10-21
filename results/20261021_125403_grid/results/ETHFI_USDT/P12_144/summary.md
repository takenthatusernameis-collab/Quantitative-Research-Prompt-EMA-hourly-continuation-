# EMA Hourly Continuation — ETHFI/USDT P12_144

**Symbol:** ETHFI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.7865 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 0.9046 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -1.6465 |
| sortino_ratio | -0.4557 |
| max_drawdown | 0.4462 |
| cagr | -0.1903 |
| net_avg_win | 85.1960 |
| net_avg_loss | -95.4470 |
| avg_hold_time_bars | 38.9658 |
| exposure | 0.6730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
