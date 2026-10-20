# EMA Hourly Continuation — MINA/USDT P34_144

**Symbol:** MINA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.7031 |
| net_win_rate | 0.5122 |
| gross_profit_factor | 1.0457 |
| gross_win_rate | 0.5167 |
| sharpe_ratio | -2.1793 |
| sortino_ratio | -0.6443 |
| max_drawdown | 0.6018 |
| cagr | -0.2712 |
| net_avg_win | 56.4238 |
| net_avg_loss | -84.2860 |
| avg_hold_time_bars | 22.2183 |
| exposure | 0.4535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
