# EMA Hourly Continuation — CARV/USDT P55_144

**Symbol:** CARV/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.6048 |
| net_win_rate | 0.4449 |
| gross_profit_factor | 0.8036 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -2.7428 |
| sortino_ratio | -0.6897 |
| max_drawdown | 0.4822 |
| cagr | -0.2708 |
| net_avg_win | 64.0670 |
| net_avg_loss | -84.8927 |
| avg_hold_time_bars | 14.8228 |
| exposure | 0.2119 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
