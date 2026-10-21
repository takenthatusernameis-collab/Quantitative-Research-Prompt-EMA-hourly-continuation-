# EMA Hourly Continuation — TIA/USDT P20_21

**Symbol:** TIA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 109 |
| net_profit_factor | 0.8182 |
| net_win_rate | 0.5229 |
| gross_profit_factor | 1.0852 |
| gross_win_rate | 0.5229 |
| sharpe_ratio | -0.6264 |
| sortino_ratio | -0.0943 |
| max_drawdown | 0.1424 |
| cagr | -0.0428 |
| net_avg_win | 82.0838 |
| net_avg_loss | -109.9651 |
| avg_hold_time_bars | 4.1101 |
| exposure | 0.0204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
