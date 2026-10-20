# EMA Hourly Continuation — MANTA/USDT P8_26

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1536 |
| net_profit_factor | 0.5721 |
| net_win_rate | 0.4518 |
| gross_profit_factor | 1.0003 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -8.8463 |
| sortino_ratio | -4.8840 |
| max_drawdown | 0.9975 |
| cagr | -0.9076 |
| net_avg_win | 19.2189 |
| net_avg_loss | -27.6872 |
| avg_hold_time_bars | 4.1868 |
| exposure | 0.2923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
