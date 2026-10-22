# EMA Hourly Continuation — PYTH/USDT P34_144

**Symbol:** PYTH/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.7583 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 1.0428 |
| gross_win_rate | 0.5083 |
| sharpe_ratio | -1.9430 |
| sortino_ratio | -0.6103 |
| max_drawdown | 0.5420 |
| cagr | -0.2464 |
| net_avg_win | 65.6443 |
| net_avg_loss | -87.2882 |
| avg_hold_time_bars | 18.0331 |
| exposure | 0.3967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
